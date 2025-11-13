from fastapi import status


def test_root_endpoint(client):
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Digital Signature Service running."}


def test_ping_endpoint(client):
    response = client.get("/api/ping")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "ok"}
