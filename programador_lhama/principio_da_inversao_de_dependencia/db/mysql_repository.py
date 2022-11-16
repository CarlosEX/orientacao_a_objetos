from .interface import Repository

class MySqlRepository(Repository):

    def inserir(self, dado) -> None:
        print('Inserindo {} no banco de Mysql'.format(dado))

    def deletar(self, dado) -> None:
        print('Inserindo {} no banco de Mysql'.format(dado))

    