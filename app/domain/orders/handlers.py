from app.domain.orders.events import ChangeStatus
from app.services.events.base import EventHandler


class SendMessage(EventHandler):
    def run(self, db, event: ChangeStatus):
        """Генерация сообщения исходя из статуса и вызов Celery таски на отправку сообщений."""


PRODUCT_EVENTS_HANDLERS = {
    ChangeStatus: [SendMessage]
}
