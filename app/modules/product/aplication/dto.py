from dataclasses import dataclass
from typing import Optional
from pydantic import ConfigDict, BaseModel


class ProductRequestDTO(BaseModel):
    category: str
    description: str
    name: str
    cost: float
    third_party_id: Optional[int] = None

    model_config = ConfigDict(json_schema_extra={
        "example": {
            "category": "Suplementos",
            "description": "Proteina en polvo a base de suero de leche",
            "name": "Proteina",
            "cost": 100000
        }
    })


@dataclass(frozen=True)
class ProductResponseDTO(BaseModel):
    id: int
    third_party_id: int
    category: str
    description: str
    name: str
    is_active: bool
    cost: float
    model_config = ConfigDict(from_attributes=True)
