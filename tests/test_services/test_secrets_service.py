import json
import pytest
from fastapi import HTTPException, status
from unittest.mock import patch
from app.seedwork.infrastructure.utils import get_secrets


class TestGetSecrets:
    @patch('app.seedwork.infrastructure.utils.boto3')
    def test_get_secrets_success(self, mock_boto3):
        mock_client = mock_boto3.client()
        mock_response = {'SecretString': json.dumps({'key': 'value'})}
        mock_client.get_secret_value.return_value = mock_response
        mock_boto3.session.Session().client.return_value = mock_client
        secrets = get_secrets()

        assert secrets == {'key': 'value'}

    @patch('app.seedwork.infrastructure.utils.boto3')
    def test_get_secrets_exception(self, mock_boto3):
        mock_client = mock_boto3.client()
        mock_client.get_secret_value.side_effect = Exception('Error de prueba')
        mock_boto3.session.Session().client.return_value = mock_client
        with pytest.raises(HTTPException) as exc_info:
            get_secrets()

        assert exc_info.value.status_code == status.HTTP_401_UNAUTHORIZED
