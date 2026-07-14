class AIProviderError(Exception):
    """Base exception for AI gateway failures."""


class ProviderNotFoundError(AIProviderError):
    """Raised when a requested provider is not registered."""


class ProviderConfigurationError(AIProviderError):
    """Raised when a provider is misconfigured."""
