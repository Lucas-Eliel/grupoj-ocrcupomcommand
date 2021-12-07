from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

if __name__ == '__main__':
    key = ''

    credentials = CognitiveServicesCredentials(key)
    client = ComputerVisionClient(
        endpoint="https://ocr-cupom.cognitiveservices.azure.com/",
        credentials=credentials
    )

    domain = "landmarks"

    image = open("/Users/lucaseliel/Desktop/cupom-fiscal.jpeg", "rb")

    textos = client.recognize_printed_text_in_stream(image, language="pt")

    for region in textos.regions:
        for line in region.lines:
            linha_texto = ''
            for palavra in line.words:
                linha_texto += palavra.text + ''
            print(linha_texto.rstrip())