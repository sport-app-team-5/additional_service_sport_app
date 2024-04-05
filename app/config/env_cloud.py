from app.seedwork.infrastructure.utils import get_secrets

secrets = get_secrets()


class Env:
    PROJECT_NAME: str = "Additional Service SportApp"
    PROJECT_VERSION: str = "1.0.0"
    DB_ENGINE: str = "postgresql"

    try:
        SECRET_KEY: str = secrets["SECRET_KEY"]
        ENV: str = secrets["ENV"]

        DB_USER: str = secrets["DB_USER"]
        DB_PASSWORD: str = secrets["DB_PASSWORD"]
        DB_HOST: str = secrets["DB_HOST"]
        DB_PORT: str = secrets["DB_PORT"]
        DB_NAME: str = secrets["DB_NAME"]
        DATABASE_URL = f"{DB_ENGINE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:" \
                       f"{DB_PORT}/{DB_NAME}"

        AWS_ACCESS_KEY_ID = secrets["AWS_ACCESS_KEY_ID"]
        AWS_SECRET_ACCESS_KEY = secrets["AWS_SECRET_ACCESS_KEY"]
        TOPIC_ARN = secrets["TOPIC_ARN"]

    except KeyError as e:
        raise KeyError(f"Missing {e} in secrets")


env = Env
