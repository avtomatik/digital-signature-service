from datetime import datetime

from fastapi import status

from app.api.schemas import SignResponse


def test_sign_endpoint(client, generate_document_payload):
    _, payload = generate_document_payload

    response = client.post("/api/sign", json=payload.model_dump())
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    for key in SignResponse.model_fields.keys():
        assert key in data

    assert data["document_id"] == payload.document_id
    assert "signature_value" in data
    datetime.fromisoformat(data["signed_at"])
