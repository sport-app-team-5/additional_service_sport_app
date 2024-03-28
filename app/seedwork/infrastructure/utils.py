import json
import boto3
from fastapi import HTTPException, status

SECRET_NAME_AWS = "user_backend"
REGION_AWS = "us-east-1"
SERVICE_NAME_AWS = "secretsmanager"


def get_secrets() -> dict:
    try:
        session = boto3.session.Session()
        client = session.client(service_name=SERVICE_NAME_AWS, region_name=REGION_AWS)

        response = client.get_secret_value(SecretId=SECRET_NAME_AWS)
        secret_string = response['SecretString']
        secrets = json.loads(secret_string)

        return secrets
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
