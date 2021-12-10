from azure.ai.formrecognizer import FormRecognizerClient
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.core.credentials import AzureKeyCredential
from msrest.authentication import CognitiveServicesCredentials

if __name__ == '__main__':
    endpoint = "https://ocr-form.cognitiveservices.azure.com/"
    credential = AzureKeyCredential("")

    form_recognizer_client = FormRecognizerClient(endpoint, credential)

    image = open("/Users/lucaseliel/Desktop/cupom-fiscal.jpeg", "rb")

    report = form_recognizer_client.begin_recognize_receipts(image)

    dados = report.result()

    recibo = dados[0]

    if recibo.fields.get("MerchantAddress").value is not None:
        print(recibo.fields.get("MerchantAddress").value)

    if recibo.fields.get("MerchantName").value is not None:
        print(recibo.fields.get("MerchantName").value)

    if recibo.fields.get("Total").value is not None:
        print(recibo.fields.get("Total").value)

    for item in recibo.fields.get("Items").value:
        item_name = item.value.get("Name")
        print(item_name.value)

        item_price = item.value.get("Price")
        print(item_price.value)

    print(recibo.fields)
