from abc import ABC
from app.seedwork.domain.repositories import Repository


class ServicesRepository(Repository, ABC):
    ...


class EventRepository(Repository, ABC):
    ...
        