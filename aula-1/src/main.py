

class Autor:
    nome: str


# Classe
class Livro:
    # Atributos
    titulo: str
    autor: Autor
    ano_publi: int
    num_pag: int
    genero: str
    alugado: bool
    comprado: bool

    # Métodos
    def comprar(self):
        pass


class Biblioteca:
    livros: [Livro]

    def adicionar_livro(self):
        print("Adicionar")

    def remover_livro(self):
        pass

    def exibir_livros(self):
        pass


# Objeto
biblioteca = Biblioteca()
biblioteca.adicionar_livro()
