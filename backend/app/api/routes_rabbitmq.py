import uuid
from datetime import datetime, timezone

from fastapi import APIRouter

from app.api.schemas import SignRequest
from app.services.rabbitmq import rabbitmq_service

router = APIRouter()


@router.post("/sign-async")
async def sign_async(request: SignRequest):
    message = {
        "document_id": request.document_id,
        "payload": request.payload,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "signature_id": str(uuid.uuid4()),
    }
    await rabbitmq_service.publish_message("signing_queue", message)
    return {"status": "queued", "message": "Document signing task is queued."}
