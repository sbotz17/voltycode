from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    provider: str = "openai"
    messages: list[ChatMessage]
    model: str | None = None
    system_prompt: str | None = None
    temperature: float = 0.7
    max_tokens: int | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class ChatResponse(BaseModel):
    provider: str
    model: str | None = None
    message: ChatMessage
    metadata: dict[str, Any] = Field(default_factory=dict)


class ModelInfo(BaseModel):
    id: str
    name: str
    provider: str
    context_window: int | None = None


class ProviderHealth(BaseModel):
    provider: str
    status: str
    message: str
