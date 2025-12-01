import random
import string

import pytest
from fastapi.testclient import TestClient

from app.api.schemas import SignRequest
from app.main import app


@pytest.fixture(scope="module")
def client():
    return TestClient(app)


@pytest.fixture
def generate_document_payload():
    """Fixture to generate document_id and SignRequest payload."""
    document_id = "".join(
        random.choices(string.ascii_letters + string.digits, k=8)
    )

    payload = SignRequest(document_id=document_id, payload="Hello world!")
    return document_id, payload
