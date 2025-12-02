from datetime import datetime

from pydantic import BaseModel, ConfigDict


class SignRequest(BaseModel):
    document_id: str
    payload: str

    class Config(ConfigDict):
        from_attributes = True


class SignResponse(BaseModel):
    signature_id: str
    document_id: str
    signed_at: datetime
    signature_value: str

    class Config(ConfigDict):
        from_attributes = True
