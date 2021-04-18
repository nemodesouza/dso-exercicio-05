from abc import ABC, abstractmethod
from animal import Animal


class Ave(ABC, Animal):

    def __init__(self, tamanho_passo: int, altura_voo: int):
        # Ave(int tamanho_passo, int altura_voo)
        super().__init__(tamanho_passo)
        self.__tamanho_passo = tamanho_passo
        self.__altura_voo = altura_voo
        self.__deslocamento = 0

    @property
    def tamanho_passo(self):
        return self.__tamanho_passo

    @tamanho_passo.setter
    def tamanho_passo(self, tamanho_passo):
        self.__tamanho_passo = tamanho_passo

    @property
    def altura_voo(self):
        return self.__altura_voo

    @altura_voo.setter
    def altura_voo(self, altura_voo):
        self.__altura_voo = altura_voo


    def mover(self, distancia):
        if isinstance(distancia, int):
            self.__deslocamento = self.__tamanho_passo * distancia

        return self.__deslocamento
