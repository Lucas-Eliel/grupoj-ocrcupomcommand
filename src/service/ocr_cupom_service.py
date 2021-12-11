from azure.ai.formrecognizer import FormRecognizerClient
from azure.core.credentials import AzureKeyCredential

from src.model.cupom import Cupom
from src.repository.ocr_cupom_repository import OcrCupomRepository
from src.service.classifica_cupom_service import ClassificaCupomService
from src.utils.validation_request import ValidationRequest


def get_client_form_recognizer():
    endpoint = "https://ocr-form.cognitiveservices.azure.com/"
    credential = AzureKeyCredential("")
    return FormRecognizerClient(endpoint, credential)


class OcrCupomService:

    def __init__(self, event):
        self.event = event
        self.repository = OcrCupomRepository()
        self.validation = ValidationRequest(event)
        self.client_form_recognizer = get_client_form_recognizer()
        self.service = ClassificaCupomService

    def process_cupom(self):
        self.validation.validate_body()

        body = self.event['body']
        cupom_image = body['cupom']

        report = self.client_form_recognizer.begin_recognize_receipts(cupom_image)
        result = report.result()
        dados_recognizer = result[0]

        cupom = Cupom(dados_recognizer)

        self.service.classificar(cupom)

        self.repository.save(cupom)

        return {
            "id": cupom.id
        }
