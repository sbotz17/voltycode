from __future__ import annotations

from collections.abc import AsyncIterator

from ..base import AIProvider
from ..models import ChatRequest, ChatResponse, ChatMessage, ModelInfo, ProviderHealth


class OpenRouterProvider(AIProvider):
    name = "openrouter"

    async def chat(self, request: ChatRequest) -> ChatResponse:
        request = self._coerce_request(request)
        content = "OpenRouter provider placeholder response"
        if request.messages:
            content = f"OpenRouter: {request.messages[-1].content}"
        return ChatResponse(
            provider=self.name,
            model=request.model or "openai/gpt-4o-mini",
            message=ChatMessage(role="assistant", content=content),
            metadata={"provider": self.name},
        )

    async def stream(self, request: ChatRequest) -> AsyncIterator[str]:
        yield (await self.chat(request)).message.content

    async def models(self) -> list[ModelInfo]:
        return [
            ModelInfo(id="openai/gpt-4o-mini", name="OpenAI GPT-4o mini", provider=self.name),
            ModelInfo(id="anthropic/claude-3.5-sonnet", name="Anthropic Claude 3.5 Sonnet", provider=self.name),
        ]

    async def health(self) -> ProviderHealth:
        return ProviderHealth(provider=self.name, status="ok", message="Provider ready")
