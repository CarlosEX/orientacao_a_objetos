class PessoaA:

    def se_apresenta(self):
        print('Olá, sou a pessoa A')

class PessoaB(PessoaA):

    def __init__(self) -> None:
        super().__init__()
        
    def se_apresenta(self):
        print('Olá, sou a pessoa B')
