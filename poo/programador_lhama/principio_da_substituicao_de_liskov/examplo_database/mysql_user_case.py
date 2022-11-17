from mysql import Mysql
from typing import Type

class MysqlUserCase(Mysql):

    def __init__(self) -> None:
        super().__init__()

    def buscar(self, db_repo:Type[Mysql]):
        db_repo.select()