from __future__ import annotations

from collections.abc import AsyncIterator

from ..base import AIProvider
from ..models import ChatRequest, ChatResponse, ChatMessage, ModelInfo, ProviderHealth


class GroqProvider(AIProvider):
    name = "groq"

    async def chat(self, request: ChatRequest) -> ChatResponse:
        request = self._coerce_request(request)
        content = "Groq provider placeholder response"
        if request.messages:
            content = f"Groq: {request.messages[-1].content}"
        return ChatResponse(
            provider=self.name,
            model=request.model or "llama-3.1-8b",
            message=ChatMessage(role="assistant", content=content),
            metadata={"provider": self.name},
        )

    async def stream(self, request: ChatRequest) -> AsyncIterator[str]:
        yield (await self.chat(request)).message.content

    async def models(self) -> list[ModelInfo]:
        return [
            ModelInfo(id="llama-3.1-8b", name="Llama 3.1 8B", provider=self.name),
            ModelInfo(id="llama-3.1-70b", name="Llama 3.1 70B", provider=self.name),
        ]

    async def health(self) -> ProviderHealth:
        return ProviderHealth(provider=self.name, status="ok", message="Provider ready")
