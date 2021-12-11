class Estabelecimento:

    def __init__(self, dados_recognizer):
        self.cpf_cnpj = ""
        self.nome = ""
        self.endereco = ""
        self.dados_recognizer = dados_recognizer

    def to_dict(self):

        if self.dados_recognizer.fields.get("MerchantAddress").value is not None:
            self.endereco = self.dados_recognizer.fields.get("MerchantAddress").value

        if self.dados_recognizer.fields.get("MerchantName").value is not None:
            self.nome = self.dados_recognizer.fields.get("MerchantName").value

        return {
            "cpf_cnpj": self.cpf_cnpj,
            "nome": self.nome,
            "endereco": self.endereco,
        }