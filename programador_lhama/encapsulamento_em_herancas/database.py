class DatabaseConn:

    def __init__(self) -> None:
        self.__database = 'Postgres'
        self._conn = '//connection_string'
        self.user = 'Lhama'

    def get_database(self) -> None:
        print(self.__database)

    def _testing_connection(self) -> None:
        print('Conneciton OK!')