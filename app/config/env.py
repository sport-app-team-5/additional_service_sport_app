import os
from dotenv import load_dotenv

load_dotenv()


class Env:
    DB_ENGINE: str = "postgresql"

    SECRET_KEY: str = os.getenv("SECRET_KEY", "secret")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "local")

    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: str = os.getenv("DB_PORT", 5432)
    DB_NAME: str = os.getenv("DB_NAME")
    DATABASE_URL = f"{DB_ENGINE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:" \
                   f"{DB_PORT}/{DB_NAME}"


env = Env
