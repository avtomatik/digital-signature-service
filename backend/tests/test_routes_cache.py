import pytest
from fastapi import status

from app.services import redis as redis_service
from tests.fakes.fake_redis import FakeRedis


@pytest.fixture(autouse=True)
def mock_redis(monkeypatch):
    fake = FakeRedis()
    monkeypatch.setattr(redis_service, "redis_client", fake)
    return fake


def test_cache_test(client):
    response = client.get("/api/cache/cache-test")
    assert response.status_code == status.HTTP_200_OK

    data = response.json()
    assert "cached_value" in data
    assert data["cached_value"] == "Hello, Redis!"
