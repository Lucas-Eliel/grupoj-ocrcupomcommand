class Consumidor:

    def __init__(self, dados_recognizer):
        self.cpf_cnpj = ""
        self.nome = ""
        self.dados_recognizer = dados_recognizer

    def to_dict(self):
        return {
            "cpf_cnpj": self.cpf_cnpj,
            "nome": self.nome,
        }