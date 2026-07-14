from __future__ import annotations

from .base import AIProvider
from .exceptions import ProviderNotFoundError
from .providers import (
    AnthropicProvider,
    GeminiProvider,
    GroqProvider,
    OllamaProvider,
    OpenAIProvider,
    OpenRouterProvider,
)


class ProviderRegistry:
    """Registry that resolves provider implementations by name."""

    def __init__(self) -> None:
        self._providers: dict[str, AIProvider] = {}
        self._register_default_providers()

    def _register_default_providers(self) -> None:
        for provider in (
            OpenAIProvider(),
            AnthropicProvider(),
            GeminiProvider(),
            GroqProvider(),
            OpenRouterProvider(),
            OllamaProvider(),
        ):
            self.register_provider(provider)

    def register_provider(self, provider: AIProvider) -> None:
        self._providers[provider.name.lower()] = provider

    def get_provider(self, provider_name: str) -> AIProvider:
        normalized_name = (provider_name or "openai").strip().lower()
        provider = self._providers.get(normalized_name)
        if provider is None:
            available = ", ".join(sorted(self._providers))
            raise ProviderNotFoundError(
                f"Unsupported provider '{provider_name}'. Available providers: {available}"
            )
        return provider

    def list_providers(self) -> list[str]:
        return sorted(self._providers)
