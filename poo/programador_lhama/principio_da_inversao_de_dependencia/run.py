from typing import Type
from db.interface import Repository
from db.mongo_repository import MongoRepository
from db.mysql_repository import MySqlRepository


class Usuario:

    def __init__(self, repositorio: Type[Repository]) -> None:
        self.__repositorio = repositorio
        

    def armazenar_dado(self, dado: any) -> None:
        self.__repositorio.inserir(dado)

    def remover_dado(self, dado: any) -> None:
        self.__repositorio.deletar(dado)


usuario = Usuario(MySqlRepository())
usuario.armazenar_dado(23)


usuario = Usuario(MongoRepository())
usuario.armazenar_dado(23)