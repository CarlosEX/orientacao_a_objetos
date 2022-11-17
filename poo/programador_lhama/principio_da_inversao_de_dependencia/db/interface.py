from abc import ABC, abstractmethod

class Repository(ABC):

    @abstractmethod
    def inserir(self, dado) -> None:
        pass

    @abstractmethod
    def deletar(self, dado) -> None:
        pass
    