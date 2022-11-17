from abstract_class import AbstracctClass

class Filha(AbstracctClass):

    def apresentar_metodo(self) -> None:
        print(self.atributo)

    def metodo_abstrato(self) -> None:
        print('Implementando metodo abstrato')

filha = Filha()
# filha.apresentar_metodo()
# filha.metodo('Estou aqui')
filha.metodo_abstrato()


# abstractClass = AbstracctClass()
# abstractClass.metodo('Fazendo algo')