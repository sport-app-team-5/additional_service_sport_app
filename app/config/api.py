from typing import Any
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    APP_VERSION: str = "1"


settings = Config()

app_configs: dict[str, Any] = {"title": "User Sport API"}
