from __future__ import annotations

from collections.abc import AsyncIterator

from ..base import AIProvider
from ..models import ChatRequest, ChatResponse, ChatMessage, ModelInfo, ProviderHealth


class AnthropicProvider(AIProvider):
    name = "anthropic"

    async def chat(self, request: ChatRequest) -> ChatResponse:
        request = self._coerce_request(request)
        content = "Anthropic provider placeholder response"
        if request.messages:
            content = f"Anthropic: {request.messages[-1].content}"
        return ChatResponse(
            provider=self.name,
            model=request.model or "claude-3-haiku",
            message=ChatMessage(role="assistant", content=content),
            metadata={"provider": self.name},
        )

    async def stream(self, request: ChatRequest) -> AsyncIterator[str]:
        yield (await self.chat(request)).message.content

    async def models(self) -> list[ModelInfo]:
        return [
            ModelInfo(id="claude-3-haiku", name="Claude 3 Haiku", provider=self.name),
            ModelInfo(id="claude-3-sonnet", name="Claude 3 Sonnet", provider=self.name),
        ]

    async def health(self) -> ProviderHealth:
        return ProviderHealth(provider=self.name, status="ok", message="Provider ready")
