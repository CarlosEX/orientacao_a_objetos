from typing import Type
from interfaces.formas import IForma

class Engenheiro:

    def __init__(self, nome: str) -> None:
        self.nome = nome

    def medir_perimetro(self, terreno: Type[IForma]):
        perimetro = terreno.get_area()
        print('{} mediu o perimetro: {} m'.format(self.nome, perimetro))

    def medir_area(self, terreno: Type[IForma]):
        area = terreno.get_area()
        print('{} mediu o area: {} m2'.format(self.nome, area))