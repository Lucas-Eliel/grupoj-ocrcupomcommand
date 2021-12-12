import uuid

from src.model.consumidor import Consumidor
from src.model.estabelecimento import Estabelecimento
from src.model.produtos import Produtos


class Cupom:

    def __init__(self, dados_recognizer):
        self.id_processo = str(uuid.uuid4())
        self.status_cupom = ""
        self.ranking = ""
        self.estabelecimento = ""
        self.consumidor = ""
        self.produtos = ""
        self.valor_total = ""
        self.dados_recognizer = dados_recognizer

        self.estabelecimento = Estabelecimento(dados_recognizer)
        self.consumidor = Consumidor(dados_recognizer)
        self.produtos = Produtos(dados_recognizer)

    def to_dict(self):
        if self.dados_recognizer.fields.get("Total").value is not None:
            self.valor_total = self.dados_recognizer.fields.get("Total").value

        return {
            "id_processo": self.id_processo,
            "status_cupom": self.status_cupom,
            "ranking": self.ranking,
            "estabelecimento": self.estabelecimento.to_dict(),
            "consumidor": self.consumidor.to_dict(),
            "produtos": self.produtos.to_dict(),
            "valor_total": self.valor_total
        }

