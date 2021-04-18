from ave import Ave
from animal import Animal

class Canarinho(Animal, Ave):

    def __init__(self, tamanho_passo: int, altura_voo: int):
        self().__init__(tamanho_passo, altura_voo)
        self.__deslocamento = 0

    def cantar(self):

        return ("CANARINHO: PRODUZ SOM: PIU")

    def mover(self):

        return ("CANARINHO: DESLOCOU ", self.__deslocamento, "VOANDO")
