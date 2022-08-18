from app.domain.orders.events import ChangeStatus
from app.services.events.event_bus import EventBus


class UpdateOrderStatusService:
    def __init__(
        self,
        *,
        db,
        order_status: "OrderStatusUpdate",
        event_bus: EventBus,  # Попадает из контроллера, там берётся из app через Depends().
    ):
        ...
        self._event_bus = event_bus

    async def execute(self):
        # Всё что угодно.
        order = ...
        prev_status = ...
        await self._raise_event(order, prev_status)

    async def _raise_event(self, order, prev_status):
        self._event_bus.handle(
            ChangeStatus(
                order_id=order.id,
                prev_ecom_status=prev_status,
                new_ecom_status=order.status_ecom,
            )
        )
