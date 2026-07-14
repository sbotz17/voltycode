from __future__ import annotations

from fastapi import APIRouter, Depends

from .exceptions import ProviderNotFoundError
from .models import ChatRequest, ChatResponse
from .registry import ProviderRegistry

router = APIRouter(prefix="", tags=["ai_gateway"])


def get_registry() -> ProviderRegistry:
    return ProviderRegistry()


@router.post("/", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    registry: ProviderRegistry = Depends(get_registry),
) -> ChatResponse:
    try:
        provider = registry.get_provider(request.provider)
    except ProviderNotFoundError as exc:
        raise exc from None

    return await provider.chat(request)
