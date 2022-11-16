class PostgresDB:
    
    def __init__(self) -> None:
        self.__conexao = 'Postegres'

    def conectar(self) -> str:
        print('Conectando ao banco de Postgres...')
        return self.__conexao

    def desconectar(self) -> str:
        print('Desconectando ao banco Postgres...')
        return self.__conexao