from abc import ABC, abstractmethod
from typing import List
from app.modules.services.aplication.dto import ServiceResponseDTO
from app.modules.services.domain.entities import Service
from app.seedwork.domain.repositories import Repository
from sqlalchemy.orm import Session


class ServicesRepository(Repository, ABC):
    ...
        
