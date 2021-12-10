import boto3

from src.exception.dynamodb_integration_exception import DynamodbIntegrationException


def get_connection_dynamodb():
    dynamodb = boto3.resource('dynamodb', endpoint_url="", region_name="sa-east-1")
    return dynamodb.Table('xxx')


class OcrCupomRepository:

    def __init__(self):
        self.connection = get_connection_dynamodb()

    def insert(self, cupom):
        try:
            self.connection.put_item(Item=cupom)
            return cupom
        except Exception as error:
            raise DynamodbIntegrationException("Error ao criar registro do cupom no DynamoDB")