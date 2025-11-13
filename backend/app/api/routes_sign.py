from app.api.schemas import SignRequest, SignResponse
from fastapi import APIRouter
from datetime import datetime, timezone
import uuid

router = APIRouter()


@router.get("/ping")
async def ping():
    return {"status": "ok"}


@router.post("/sign", response_model=SignResponse)
async def sign_document(request: SignRequest):
    fake_signature = str(uuid.uuid4()).replace("-", "")
    return SignResponse(
        signature_id=str(uuid.uuid4()),
        document_id=request.document_id,
        signed_at=datetime.now(timezone.utc),
        signature_value=f"mock-signature-{fake_signature}",
    )
