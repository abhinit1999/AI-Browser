from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_query_endpoint():
    payload = {"message": "What is LangChain used for?"}
    response = client.post("/query", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    assert isinstance(data["response"], list)
    assert any(data["response"])