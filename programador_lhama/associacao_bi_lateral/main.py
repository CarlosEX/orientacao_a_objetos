from modulos import Casa, Pessoa

casa_de_ana = Casa()
ana = Pessoa('Ana')

pedro = Pessoa('Pedro')

ana.set_local(casa_de_ana)
casa_de_ana.set_proprietario(pedro)

proprietario = casa_de_ana.get_proprietario()
ana.apresentar_local()