from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

# verify that the root endpoint works and returns the expected response
def test_root():
    response = client.get("/")

    # request must return status 200, if API return 500, pytest fails
    assert response.status_code == 200

    # converts the json response into dict
    body = response.json()

    assert body["service"] == "Nexus"
    assert body["docs"] == "/docs"
    assert body["health"] == "/api/v1/health"

def test_health():
    response = client.get("/api/v1/health")

    assert response.status_code == 200

    body = response.json()

    assert body["status"] == "ok"
    assert body["service"] == "nexus"

