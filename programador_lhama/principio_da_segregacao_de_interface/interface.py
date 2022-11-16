from abc import ABC, abstractmethod

class IAveVoadora(ABC):

    @abstractmethod
    def comer(self):
        raise 'Should implement voar method'

    @abstractmethod
    def voar(self):
        raise 'Should implement voar method'

    @abstractmethod
    def gritar(self):
        raise 'Should implement voar method'

class IAveQueNaoVoa(ABC):

    @abstractmethod
    def comer(self):
        raise 'Should implement voar method'

    @abstractmethod
    def gritar(self):
        raise 'Should implement voar method'