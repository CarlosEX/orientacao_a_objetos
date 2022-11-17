from models import Insersor, Repositorio

class RepositorioFaker(Repositorio):
    def __init__(self) -> None:
        super().__init__()

    def select(self, nome: str) -> None:
        return None

repo = RepositorioFaker()
insersor = Insersor(repo)

data = insersor.inserir_dado("Lhama", 34)
print(data)