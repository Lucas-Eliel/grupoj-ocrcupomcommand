from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import FormRecognizerClient


if __name__ == '__main__':
    endpoint = "https://ocr-form.cognitiveservices.azure.com/"
    credential = AzureKeyCredential("")

    form_recognizer_client = FormRecognizerClient(endpoint, credential)

    image = open("/Users/lucaseliel/Desktop/cupom-fiscal.jpeg", "rb")

    report = form_recognizer_client.begin_recognize_receipts(image)

    dados  = report.result()

    recibo = dados[0]

    print(recibo.fields)