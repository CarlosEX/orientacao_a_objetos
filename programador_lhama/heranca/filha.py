from mae import Mae

class Filha(Mae):

    def __init__(self) -> None:
        super().__init__('Rua do bolo')

    def brincar(self, brinquedo: str) -> None:
        print('estou brincando com {}'.format(brinquedo))


