class Casa:

    def __init__(self) -> None:
        self.__endereco = 'Rua do amor'

    def acender_luzes(self) -> None:
        print('Estou acendendo as luzes')

    def get_endereco(self) -> str:
        return self.__endereco
