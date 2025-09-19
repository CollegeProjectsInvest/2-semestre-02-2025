# classe
class Pessoa:
    # # atributos
    # nome: str      # atributo público
    # __email: str   # atributo privado
    # _idade: int  # atributo protegido

    # método construtor
    # inicializar a classe
    def __init__(self, nome: str, email: str, idade: int) -> None:
        self.nome = nome
        self.__email = email
        self._idade = idade

    # métodos
    def cadastrar(self) -> None:
        # self se refere a classe atual
        print(f"Nome: {self.nome}")
        print(f"Email: {self.__email}")
        print(f"Idade: {self._idade}")
