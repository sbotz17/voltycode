import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[5]))

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_chat_endpoint_returns_provider_response() -> None:
    response = client.post(
        "/api/v1/chat",
        json={
            "provider": "openai",
            "messages": [{"role": "user", "content": "Hello from the gateway"}],
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["provider"] == "openai"
    assert payload["message"]["role"] == "assistant"
    assert "OpenAI" in payload["message"]["content"]
