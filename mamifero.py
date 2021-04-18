from abc import ABC, abstractmethod
from animal import Animal


class Mamifero(ABC, Animal):

    def __init__(self, tamanho_passo: int, volume_som: int):
        # Mamifero(int volume_som, int tamanho_passo)
        super().__init__(tamanho_passo)
        self.__volume_som = volume_som
        self.__deslocamento = 0

    @property
    def volume_som(self):
        return self.__volume_som

    @volume_som.setter
    def volume_som(self, volume_som):
        self.__volume_som = volume_som

    @abstractmethod
    def produzir_som(self):
        pass

    def mover(self, distancia):
        if isinstance(distancia, int):
            self.__deslocamento = self.__tamanho_passo * distancia

        return self.__deslocamento
