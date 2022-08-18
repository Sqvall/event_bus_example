from dataclasses import dataclass

from app.services.events.base import Event


@dataclass
class ChangeStatus(Event):
    order_id: str
    prev_ecom_status: str
    new_ecom_status: str
    # Можно передавать сразу объект `Order`:
    # order: Order
    # prev_ecom_status: str  # если вдруг нужен целый объект заказа + доп инфа.
