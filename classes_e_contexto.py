'''class MinhaClasse:
    
    texto = 'Escrevendo aqui...'
    
    def __init__(self, nome="Carlos") -> None:
        self.meu_atributo1 = "Olá mundo"
        self.meu_atributo2 = nome
    
    def meu_metodo_statico():
        print("Olá mundo!")

    def meu_metodo(self):
        print("Oi...")
    
    @classmethod
    def info(cls):
        print(cls.texto)
        
    def dados(num1, num2):
        result = num1 * num2
        print(result)
        
        
MinhaClasse.meu_metodo_statico()
obj = MinhaClasse()
obj.meu_metodo()
print(obj.meu_atributo2)
MinhaClasse.info()
MinhaClasse.dados(3, 5)

'''


class ControleRemoto:
    
    def __init__(self, televisao, comodo) -> None:
        self.comodo = comodo
        self.televisao = televisao
        
    def avancar_canal(self):
        print('Canal Avançado')
        
    def voltar_canal(self):
        print('Voltar o canal')
        
    def escolhar_canal(self, canal):
        print('Alterar para o canal: {}'.format(canal))
        
controle_sala = ControleRemoto('sansung', 'sala')
print(controle_sala.comodo)
print(controle_sala.televisao)
controle_sala.avancar_canal()
controle_sala.escolhar_canal(12)