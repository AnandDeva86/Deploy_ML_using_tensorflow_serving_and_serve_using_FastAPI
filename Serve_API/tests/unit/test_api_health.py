from fastapi.testclient import TestClient

from Serve_API.src.main import app


client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hi there": "This API is used to consume and then serve predictions from the served model"}

