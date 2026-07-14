from __future__ import annotations

from collections.abc import AsyncIterator

from ..base import AIProvider
from ..models import ChatRequest, ChatResponse, ChatMessage, ModelInfo, ProviderHealth


class OpenAIProvider(AIProvider):
    name = "openai"

    async def chat(self, request: ChatRequest) -> ChatResponse:
        request = self._coerce_request(request)
        content = "OpenAI provider placeholder response"
        if request.messages:
            content = f"OpenAI: {request.messages[-1].content}"
        return ChatResponse(
            provider=self.name,
            model=request.model or "gpt-4o-mini",
            message=ChatMessage(role="assistant", content=content),
            metadata={"provider": self.name},
        )

    async def stream(self, request: ChatRequest) -> AsyncIterator[str]:
        yield (await self.chat(request)).message.content

    async def models(self) -> list[ModelInfo]:
        return [
            ModelInfo(id="gpt-4o-mini", name="GPT-4o mini", provider=self.name),
            ModelInfo(id="gpt-4.1", name="GPT-4.1", provider=self.name),
        ]

    async def health(self) -> ProviderHealth:
        return ProviderHealth(provider=self.name, status="ok", message="Provider ready")
