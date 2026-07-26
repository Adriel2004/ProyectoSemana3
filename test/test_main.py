from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_predict_valid_payload():
    response = client.post(
        "/predict",
        json={"input": "becas"}
    )
    assert response.status_code == 200
    assert "result" in response.json()


def test_predict_valid_error():
    response = client.post(
        "/predict",
        json={"input": "becas"}
    )
    assert response.status_code == 201
    assert "result" in response.json()