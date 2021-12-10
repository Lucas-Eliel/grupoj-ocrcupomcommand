from azure.ai.formrecognizer import FormRecognizerClient
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.core.credentials import AzureKeyCredential
from msrest.authentication import CognitiveServicesCredentials

if __name__ == '__main__':
    endpoint = "https://ocr-form.cognitiveservices.azure.com/"
    credential = AzureKeyCredential("8c82ef6cd60c4e108d38312605d4b3a5")

    form_recognizer_client = FormRecognizerClient(endpoint, credential)

    image = open("/Users/lucaseliel/Desktop/cupom-fiscal.jpeg", "rb")

    report = form_recognizer_client.begin_recognize_receipts(image)

    dados = report.result()

    recibo = dados[0]

    print(recibo.fields)

    {'Items': FormField(value_type=list, label_data=None, value_data=None, name=Items, value=[
        FormField(value_type=dictionary, label_data=None, value_data=None, name=Items, value={
            'Name': FormField(value_type=string, label_data=None, value_data=FieldData(page_number=1, text=ANEL,
                                                                                       bounding_box=[
                                                                                           Point(x=1078.0, y=801.0),
                                                                                           Point(x=1196.0, y=803.0),
                                                                                           Point(x=1195.0, y=865.0),
                                                                                           Point(x=1078.0, y=863.0)],
                                                                                       field_elements=None), name=Name,
                              value='ANEL', confidence=0.412), 'Price': FormField(value_type=float, label_data=None,
                                                                                  value_data=FieldData(page_number=1,
                                                                                                       text=6, 00,
                                                                                                       bounding_box=[
                                                                                                           Point(
                                                                                                               x=362.0,
                                                                                                               y=842.0),
                                                                                                           Point(
                                                                                                               x=481.0,
                                                                                                               y=846.0),
                                                                                                           Point(
                                                                                                               x=478.0,
                                                                                                               y=900.0),
                                                                                                           Point(
                                                                                                               x=360.0,
                                                                                                               y=896.0)],
                                                                                                       field_elements=None),
                                                                                  name=Price, value=600.0,
                                                                                  confidence=0.912),
            'Quantity': FormField(value_type=float, label_data=None, value_data=FieldData(page_number=1, text=1UN,
                  bounding_box=[Point(x=211.0, y=838.0), Point(x=286.0, y=840.0), Point(x=285.0, y=894.0),
                                Point(x=210.0, y=891.0)], field_elements=None),
        name = Quantity, value = 1.0, confidence = 0.899), 'Tota, '
    MerchantAddress
    ': FormField(value_type=string, label_data=None, value_data=FieldData(page_number=1, text=AV CRISTOVAO COLOMBO, 67 - SAVASSI, bounding_box=[Point(x=173.9, y=283.1), Point(x=1122.1, y=297.5), Point(x=1121.2, y=356.0), Point(x=173.0, y=341.7)], field_elements=None), name=MerchantAddress, value='
    AV
    CRISTOVAO
    COLOMBO, 67 - SAVASSI
    ', confidence=0.924), '
    MerchantName
    ': FormField(value_type=string, label_data=None, value_data=FieldData(page_number=1, text=LARA, bounding_box=[Point(x=307.0, y=234.0), Point(x=422.0, y=234.0), Point(x=422.0, y=289.0), Point(x=307.0, y=288.0)], field_elements=None), name=MerchantName, value='
    LARA
    ', confidence=0.508), '
    ReceiptType
    ': FormField(value_type=string, label_data=None, value_data=None, name=ReceiptType, value='
    Itemized
    ', confidence=0.984), 'Tax': FormField(value_type=float, label_data=None, value_data=FieldData(page_number=1, text=1.52, bounding_box=[Point(x=803.0, y=1237.0), Point(x=910.0, y=1243.0), Point(x=910.0, y=1297.0), Point(x=802.0, y=1293.0)], field_elements=None), name=Tax, value=1.52, confidence=0.975), '
Total
    ': FormField(value_type=float, label_data=None, value_data=FieldData(page_number=1, text=6,00, bounding_box=[Point(x=1184.0, y=917.0), Point(x=1319.0, y=917.0), Point(x=1319.0, y=987.0), Point(x=1184.0, y=987.0)], field_elements=None), name=Total, value=600.0, confidence=0.966), '
    TransactionDate
    ': FormField(value_type=date, label_data=None, value_data=FieldData(page_number=1, text=10/07/2019, bounding_box=[Point(x=23.0, y=552.0), Point(x=291.0, y=556.0), Point(x=289.0, y=622.0), Point(x=21.0, y=617.0)], field_elements=None), name=TransactionDate, value=datetime.date(2019, 7, 10), confidence=0.673)}
