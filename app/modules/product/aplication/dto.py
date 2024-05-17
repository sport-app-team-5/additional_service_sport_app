from dataclasses import dataclass
from typing import List, Optional
from pydantic import ConfigDict, BaseModel


class ProductRequestDTO(BaseModel):
    category: str
    description: str
    name: str
    cost: float
    third_party_id: Optional[int] = None
    allergies: Optional[str] = None
    category_food: Optional[str] = None

    model_config = ConfigDict(json_schema_extra={
        "example": {
            "category": "Food",
            "description": "Cominda en polvo a base de suero de leche",
            "name": "Proteina",
            "cost": 100000,
            "allergies": "Gluten,Peanuts,Shellfish,Soy",
            "category_food": "Productos lácteos",
            "third_party_id": 1,

        }
    })


@dataclass(frozen=True)
class ProductResponseDTO(BaseModel):
    id: int
    category: str
    description: str
    name: str
    cost: float
    third_party_id: Optional[int] = None
    allergies: Optional[str] = None
    category_food: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)
