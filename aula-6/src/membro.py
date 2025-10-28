# class pai
class Membro:
    def __init__(self, nome: str, idade: int, vida: int):
        self.nome = nome
        self.idade = idade
        self.vida = vida

    def pegar_kit_membro(self) -> None:
        print("Pegando kit membro")


class MembroTop:
    pass
