from app.seedwork.infrastructure.utils import get_secrets

secrets = get_secrets()


class Env:
    DB_ENGINE: str = "postgresql"

    try:
        SECRET_KEY: str = secrets["SECRET_KEY"]
        ENVIRONMENT: str = secrets["ENVIRONMENT"]

        DB_USER: str = secrets["DB_USER"]
        DB_PASSWORD: str = secrets["DB_PASSWORD"]
        DB_HOST: str = secrets["DB_HOST"]
        DB_PORT: str = secrets["DB_PORT"]
        DB_NAME: str = secrets["DB_NAME"]
        DATABASE_URL = f"{DB_ENGINE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:" \
                       f"{DB_PORT}/{DB_NAME}"

    except KeyError as e:
        raise KeyError(f"Missing {e} in secrets")


env = Env
