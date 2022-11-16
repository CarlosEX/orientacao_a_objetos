from conection import Conection

class Mysql(Conection):
    
    def __init__(self) -> None:
        super().__init__()

    def select(self) -> None:
        self.conectar()
        print('SELECT * FROM table')