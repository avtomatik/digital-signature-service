from fastapi.testclient import TestClient
from app.main import app

import pytest


@pytest.fixture(scope="module")
def client():
    return TestClient(app)
