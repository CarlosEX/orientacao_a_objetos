from pessoa import PessoaA, PessoaB

pessoa = PessoaA()
pessoa.se_apresenta()

def apresentar():
    print('Estou alterando este metodo')

pessoa.se_apresenta = apresentar
pessoa.se_apresenta()

pessoa2 = PessoaB()
pessoa2.se_apresenta()