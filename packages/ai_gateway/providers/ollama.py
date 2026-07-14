from __future__ import annotations

from collections.abc import AsyncIterator

from ..base import AIProvider
from ..models import ChatRequest, ChatResponse, ChatMessage, ModelInfo, ProviderHealth


class OllamaProvider(AIProvider):
    name = "ollama"

    async def chat(self, request: ChatRequest) -> ChatResponse:
        request = self._coerce_request(request)
        content = "Ollama provider placeholder response"
        if request.messages:
            content = f"Ollama: {request.messages[-1].content}"
        return ChatResponse(
            provider=self.name,
            model=request.model or "llama3.2",
            message=ChatMessage(role="assistant", content=content),
            metadata={"provider": self.name},
        )

    async def stream(self, request: ChatRequest) -> AsyncIterator[str]:
        yield (await self.chat(request)).message.content

    async def models(self) -> list[ModelInfo]:
        return [
            ModelInfo(id="llama3.2", name="Llama 3.2", provider=self.name),
            ModelInfo(id="phi3", name="Phi 3", provider=self.name),
        ]

    async def health(self) -> ProviderHealth:
        return ProviderHealth(provider=self.name, status="ok", message="Provider ready")
