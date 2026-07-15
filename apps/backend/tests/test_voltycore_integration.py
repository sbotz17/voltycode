from app.core.events import get_event_bus
from voltycore.events import EventBus


def test_backend_can_resolve_event_bus() -> None:
    assert isinstance(get_event_bus(), EventBus)
