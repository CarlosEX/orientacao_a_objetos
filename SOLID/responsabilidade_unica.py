class SistemaCadastral:
    
    def cadastrar(self, nome: str, idade: int) -> None:
        
        if self.__verificar_dados(nome, idade):
            self.__armazenar_usuario(nome, idade)
        else:
            self._indicar_erro()
            
    def __verificar_dados(self, nome: str, idade: int) -> bool:
        if isinstance(nome, str) and isinstance(idade, int):
            return True
        else:
            return False
        
    def __armazenar_usuario(self, nome: str, idade: int) -> None:
        print('acessando o banco de dados...')
        print('Cadastrar o Usuário {}, idade {}'.format(nome, idade))
        
    def _indicar_erro(self) -> None:
        print('dados inválidos!')
        
s = SistemaCadastral();
s.cadastrar("Carlos", 34)