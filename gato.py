from mamifero import Mamifero
from animal import Animal

class Gato(Animal, Mamifero):

    def __init__(self, tamanho_passo: int, volume_som: int):
        self().__init__(tamanho_passo, volume_som)
        self.__deslocamento = 0
        self.__tamanho_passo = 2
        self.__volume_som = 2

    def miar(self):

        return ("CACHORRO: PRODUZ SOM: ", self.__volume_som, " SOM: MIAU")

    def mover(self):

        return ("CACHORRO: DESLOCOU ", self.__deslocamento)
