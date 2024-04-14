from abc import ABC, abstractmethod
from typing import List
from app.modules.third_party.aplication.dto import ThirdPartyRequestDTO
from app.modules.third_party.domain.entities import ThirdParty
from app.seedwork.domain.repositories import Repository
from sqlalchemy.orm import Session


class ThirdPartyRepository(Repository, ABC):
    ...
