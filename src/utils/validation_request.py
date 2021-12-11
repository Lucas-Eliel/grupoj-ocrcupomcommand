from src.exception.validation_request_exception import ValidationRequestException


class ValidationRequest:

    def __init__(self, event):
        self.event = event

    def validate_body(self):
        if self.event['body'] is None:
            raise ValidationRequestException("Não foi informado nenhuma informação para o body do request")
        if not 'cupom' in self.event['body']:
            raise ValidationRequestException("Necessário informar o cupom no body da request")