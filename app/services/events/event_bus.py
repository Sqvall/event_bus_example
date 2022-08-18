from typing import Type

from app.services.events.base import Event, EventHandler


class EventBus:
    def __init__(self, db, event_handlers: dict[Type[Event], list[EventHandler]]):
        self._handlers = event_handlers
        self._db = db

    def handle(self, event: Event):
        for handle in self._handlers.get(type(event), []):
            try:
                handle.run(self._db, event)
            except Exception:
                print("Шеф, всё пропало...")
