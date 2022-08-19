from app.domain.orders.handlers import ORDERS_EVENTS_HANDLERS
from app.services.events.event_bus import EventBus


def events_wire_up(app):
    """
    Эта штука подключается в `app_startup(...)` который в main.py
    Ну или можно прям в `app_factory(...)` этот код встроить, что бы не искать место, где это должно лежать.
    """
    # Тут может надо изменить, если мы захотим из модуля товаров обрабатывать события заказов,
    #  что бы ключи не перетирались, хотя это даже звучит странно и попахивает.
    all_events = ORDERS_EVENTS_HANDLERS | ...  # новомодный merge диктов так кстати типы не теряются.
    app.state.event_bus = EventBus(app.db, all_events)
