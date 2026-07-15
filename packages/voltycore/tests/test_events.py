from voltycore.events import Event, EventBus


async def test_event_bus_publishes_to_named_handler() -> None:
    bus = EventBus()
    received: list[Event] = []

    async def handler(event: Event) -> None:
        received.append(event)

    bus.subscribe("task.created", handler)
    event = Event(name="task.created", payload={"task_id": "123"})
    await bus.publish(event)
    assert received == [event]


async def test_event_bus_supports_wildcard_handler() -> None:
    bus = EventBus()
    received: list[str] = []

    def handler(event: Event) -> None:
        received.append(event.name)

    bus.subscribe("*", handler)
    await bus.publish(Event(name="workspace.changed"))
    assert received == ["workspace.changed"]
