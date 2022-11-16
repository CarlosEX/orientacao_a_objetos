from .interface import Repository

class MongoRepository(Repository):

    def inserir(self, dado) -> None:
        print('Inserindo {} no banco de Mongo'.format(dado))

    def deletar(self, dado) -> None:
        print('Inserindo {} no banco de Mongo'.format(dado))

    