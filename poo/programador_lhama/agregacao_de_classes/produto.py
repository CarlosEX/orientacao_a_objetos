class Produto:

    def __init__(self, nome: str, valor: float) -> None:
        self.__nome = nome
        self.__valor = valor
    
    def informacoes_produto(self) -> None:
        print('Produto: {} / valor: R$ {}'.format(self.__nome, self.__valor))
    