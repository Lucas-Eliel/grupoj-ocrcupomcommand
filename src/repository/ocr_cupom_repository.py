import boto3

from src.exception.dynamodb_integration_exception import DynamodbIntegrationException


def get_connection_dynamodb():
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:4569", region_name="sa-east-1", aws_access_key_id="admin", aws_secret_access_key="admin")
    return dynamodb.Table('ocr-cupom')


class OcrCupomRepository:

    def __init__(self):
        self.connection = get_connection_dynamodb()

    def save(self, cupom):
        try:
            self.connection.put_item(Item=cupom)
        except Exception as error:
            raise DynamodbIntegrationException("Error ao criar registro do cupom no DynamoDB")