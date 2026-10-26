
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200

    result = response.json()
    assert result["status"] == "healthy"
    assert result["model_loaded"] is True


def test_valid_iris_prediction():
    payload = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200

    result = response.json()
    assert "prediction" in result
    assert result["prediction"] in [0, 1, 2]
