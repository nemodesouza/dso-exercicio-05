from mamifero import Mamifero
from animal import Animal

class Cachorro(Animal, Mamifero):

    def __init__(self, tamanho_passo: int, volume_som: int):
        self().__init__(tamanho_passo, volume_som)
        self.__deslocamento = 0
        self.__tamanho_passo = 3
        self.__volume_som = 3

    def latir(self):

        return ("CACHORRO: PRODUZ SOM: ", self.__volume_som, " SOM: AU")

    def mover(self):

        return ("CACHORRO: DESLOCOU ", self.__deslocamento)
