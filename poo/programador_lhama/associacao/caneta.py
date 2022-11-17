from tinta import Tinta
from typing import Type

class Caneta:
    
    def __init__(self, nome: str, tamanho: float, tinta: Type[Tinta]):
        self.__nome = nome
        self.__tamanho = tamanho
        self.__tinta = tinta
        
    def get_nome(self) -> str:
        return self.__nome
    
    def print_nome(self) -> None:
        print(self.__nome)
        
    def get_tamnho(self) -> float:
        return self.__tamanho
    
    def print_tamanho(self) -> None:
        print(self.__tamanho)

    def get_tinta(self) -> Tinta :
        return self.__tinta
    
tinta = Tinta('azul', 'bic')
caneta = Caneta('Compact', 0.23, tinta)
result = caneta.get_tinta()

print('A cor: {}, com a marca: {}'.format(result.cor, result.marca) )
