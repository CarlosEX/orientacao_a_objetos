class Calculadora:
    
    def calcular(self, op, a, b):
        if op == '+':
            return self.__adicionar(a, b)
        elif op == '-':
            return self.__subtrair(a, b)
        else:
            print('Operação Inválida')

    def __adicionar(self, n1, n2):
        return n1 * n2
    
    def __subtrair(self, n1, n2):
        return n1 - n2
    
calc = Calculadora()
resultado = calc.calcular('-', 9, 6)

print(resultado)