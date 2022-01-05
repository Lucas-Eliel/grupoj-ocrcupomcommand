import json
import base64
from decimal import Decimal

from azure.ai.formrecognizer import FormRecognizerClient
from azure.core.credentials import AzureKeyCredential
from src.model.cupom import Cupom
from src.repository.ocr_cupom_repository import OcrCupomRepository
from src.service.classifica_cupom_service import ClassificaCupomService
from src.utils.validation_request import ValidationRequest


def get_client_form_recognizer():
    endpoint = "https://ocr-cupom-form.cognitiveservices.azure.com/"
    credential = AzureKeyCredential("af4bd5a411514f3cbd6c46c62841dba6")
    return FormRecognizerClient(endpoint, credential)


class OcrCupomService:

    def __init__(self, event):
        self.event = event
        self.repository = OcrCupomRepository()
        self.validation = ValidationRequest(event)
        self.client_form_recognizer = get_client_form_recognizer()

    def process_cupom(self):
        if(type(self.event['body']) == dict):
            body = self.event['body']
        else:
            body = json.loads(self.event['body'])

        self.validation.validate_body(body)

        cupom_image = body['cupom']
        cnpj = body['cnpj']

        encode_image = cupom_image.encode("ascii")
        bytes_image = base64.decodebytes(encode_image)

        report = self.client_form_recognizer.begin_recognize_receipts(bytes_image)
        result = report.result()
        dados_recognizer = result[0]

        cupom = Cupom(dados_recognizer, cnpj).to_dict()

        ClassificaCupomService(cupom).classificar()

        cupom_entity = json.loads(json.dumps(cupom), parse_float=Decimal)

        self.repository.save(cupom_entity)

        return {
            "id_processo": cupom['id_processo']
        }