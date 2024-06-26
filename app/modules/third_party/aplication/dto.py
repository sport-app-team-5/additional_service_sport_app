from dataclasses import dataclass
from pydantic import ConfigDict, BaseModel


@dataclass(frozen=True)
class ThirdPartyRequestDTO(BaseModel):
    user_id: int

    model_config = ConfigDict(json_schema_extra={
        "example": {
            "user_id": 1            
        }
    })


@dataclass(frozen=True)
class ThirdPartyResponseDTO(BaseModel):
    id: int
    user_id: int
    model_config = ConfigDict(from_attributes=True)
