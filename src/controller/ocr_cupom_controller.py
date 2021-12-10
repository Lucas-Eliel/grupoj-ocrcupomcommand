from http import HTTPStatus

from src.exception.dynamodb_integration_exception import DynamodbIntegrationException
from src.exception.validation_request_exception import ValidationRequestException
from src.service.ocr_cupom_service import OcrCupomService
from src.utils.response_utils import ResponseUtils


class OcrCupomCommandController:

    def __init__(self, event):
        self.event = event
        self.service = OcrCupomService()

    def invoke(self):
        try:
            if self.event['resource'] == '/processamento-ocr-cupom':
                if self.event['httpMethod'] == 'POST':
                    return self.service.process_cupom()
                raise ValidationRequestException("Método HTTP inválido")
            raise ValidationRequestException("Endpoint inválido")
        except ValidationRequestException as error:
            return ResponseUtils.error(HTTPStatus.BAD_REQUEST, error.message)
        except DynamodbIntegrationException as error:
            return ResponseUtils.error(HTTPStatus.SERVICE_UNAVAILABLE, error.message)



