import json
import boto3
from fastapi import HTTPException, status

SECRET_NAME_AWS = "user_backend"


def get_secrets() -> dict:
    try:
        secrets_manager_client = boto3.client('secretsmanager')
        secrets = secrets_manager_client.get_secret_value(SecretId=SECRET_NAME_AWS)
        secrets_string = secrets['SecretString']
        secrets_data = json.loads(secrets_string)
        return secrets_data
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
