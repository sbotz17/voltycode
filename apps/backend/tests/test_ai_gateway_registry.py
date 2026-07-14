
import pytest
from packages.ai_gateway.registry import ProviderRegistry


@pytest.mark.asyncio
async def test_registry_returns_requested_provider() -> None:
    registry = ProviderRegistry()
    provider = registry.get_provider("anthropic")

    response = await provider.chat(
        type(
            "Req",
            (),
            {
                "provider": "anthropic",
                "messages": [{"role": "user", "content": "Hi"}],
                "model": None,
                "system_prompt": None,
                "temperature": 0.7,
                "max_tokens": None,
                "metadata": {},
            },
        )()
    )

    assert response.provider == "anthropic"
    assert response.message.role == "assistant"
    assert "Anthropic" in response.message.content
