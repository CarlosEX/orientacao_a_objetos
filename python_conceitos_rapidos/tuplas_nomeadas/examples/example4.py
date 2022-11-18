from collections import namedtuple
from typing import Tuple, Dict, List

class NamedTuple:

    """Syntax NamedeTuple
    Syntaxe: namedetuple(typename, field_names, *, rename=False, defaults=None, module=None)
    """

    def __init__(self) -> None:

        self.__carro = namedtuple('Carro', ['Marca', 'Modelo'])
        self.__estudo = namedtuple('Estudo', ['Topico', 'Website'])

    def exemplo_simples(self):

        meu_carro = self.__carro("Fusca", "Ford")
        meu_estudo = self.__estudo('Python', 'Namedlist')

        # imprime valores da lista
        print(meu_carro)
        print(meu_estudo)

        # imprime com base no elemento/label nomeada
        print(meu_carro.Marca)
        print(meu_estudo.Topico)

        # imprime com base no índece
        print(meu_carro[0])
        print(meu_estudo[1])

        # imprime com base na função getattr
        print(getattr(meu_carro, 'Marca'))
        print(getattr(meu_carro, 'Modelo'))

        # imprime nomes dos campos da litsta
        print(meu_carro._fields)

        # altera o nome do campos da lista
        print(meu_carro._replace(Marca='Fabricante'))

        # convert um element interavel em uma tupla
        meu_carro._make(['Gol', 'Fiat'])
        print(meu_carro)

        # criar um dicinário, apartir de uma tuplenomedada
        my_dick = meu_carro._asdict
        print(my_dick)

    
