class VoltyCodeError(Exception):
    """Base exception for expected VoltyCode failures."""


class ConfigurationError(VoltyCodeError):
    """Raised when configuration is missing or invalid."""


class ProviderError(VoltyCodeError):
    """Raised when an external provider fails."""
