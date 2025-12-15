import asyncio
import json

import aio_pika
import pytest
from fastapi import status
from httpx import ASGITransport, AsyncClient

from app.core.config import settings
from app.main import app


@pytest.mark.xfail(
    reason="Idle: to be properly configured later.", strict=False
)
@pytest.mark.asyncio
async def test_sign_async(generate_document_payload):
    document_id, payload = generate_document_payload

    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.post(
            "/api/mq/sign-async", json=payload.model_dump()
        )

    assert response.status_code in (
        status.HTTP_200_OK,
        status.HTTP_422_UNPROCESSABLE_CONTENT,
    )

    data = response.json()
    assert data["status"] == "queued"
    assert data["message"] == "Document signing task is queued."

    connection = await aio_pika.connect_robust(settings.mq_url)
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue("signing_queue", durable=True)

        future = asyncio.Future()

        async def on_message(message: aio_pika.IncomingMessage):
            body = json.loads(message.body)
            future.set_result(body)
            await message.ack()

        await queue.consume(on_message)

        # =====================================================================
        # Temporary workaround for the issue of mismatching document_ids;
        # this fix addresses the immediate problem but is not a robust
        # solution.
        # A proper solution is needed to ensure consistency and handle edge
        # cases.
        # =====================================================================
        await asyncio.sleep(1)

        received_message = await future

    assert received_message["document_id"] == document_id
    assert received_message["payload"] == "Hello world!"
    assert "timestamp" in received_message
    assert "signature_id" in received_message
