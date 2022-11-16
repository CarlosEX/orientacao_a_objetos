class Pessoa:
    
    def __init__(self, nome, idade, cpf) -> None:
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf

    def corret(self):
        print('Estou correndo')
        
    def beber(self, bebida):
        if bebida == 'cerveja':
            self.__apresentar_documento()
        print('bebendo...')
        
    def __apresentar_documento(self):
        print(self.__cpf)
        
        
ronaldo = Pessoa('Carlos', 32, 'df984430948')
print(ronaldo.nome)
print(ronaldo.idade)
ronaldo.beber('cerveja')
ronaldo.beber('suco')