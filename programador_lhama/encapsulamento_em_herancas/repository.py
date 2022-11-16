from database import DatabaseConn

class Repository(DatabaseConn):

    def __init__(self) -> None:
        super().__init__()

    def select(self) -> None:
        self._testing_connection()
        print('connection to {}'.format(self._conn))
        print('SELECT * FROM table')
        print(self.user)