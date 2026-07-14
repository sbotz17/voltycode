from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import AsyncIterator
from typing import Any

from .models import ChatRequest, ChatResponse, ModelInfo, ProviderHealth


class AIProvider(ABC):
    """Abstract contract for all AI providers."""

    name: str = ""

    @staticmethod
    def _coerce_request(request: ChatRequest | dict[str, Any] | Any) -> ChatRequest:
        if isinstance(request, ChatRequest):
            return request
        return ChatRequest.model_validate(request, from_attributes=True)

    @abstractmethod
    async def chat(self, request: ChatRequest) -> ChatResponse:
        """Execute a single completion request."""

    @abstractmethod
    async def stream(self, request: ChatRequest) -> AsyncIterator[str]:
        """Stream a completion response incrementally."""

    @abstractmethod
    async def models(self) -> list[ModelInfo]:
        """Return a provider-specific list of available models."""

    @abstractmethod
    async def health(self) -> ProviderHealth:
        """Report the provider health status."""
