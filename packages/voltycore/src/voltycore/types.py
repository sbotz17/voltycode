from datetime import UTC, datetime
from typing import NewType
from uuid import UUID

EntityId = NewType("EntityId", UUID)


def utc_now() -> datetime:
    return datetime.now(UTC)
