from abc import ABC, abstractmethod
from typing import List
from sqlalchemy.orm import Session
from .entities import Entity


class Repository(ABC):
    ...