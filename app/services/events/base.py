import abc
from dataclasses import dataclass


@dataclass
class Event:
    ...


class EventHandler(abc.ABC):
    @abc.abstractmethod
    def run(self, db, event: Event):
        ...
