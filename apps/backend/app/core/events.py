from functools import lru_cache

from voltycore.events import EventBus


@lru_cache
def get_event_bus() -> EventBus:
    return EventBus()
