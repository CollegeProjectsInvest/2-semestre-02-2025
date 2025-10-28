from membro import Membro, MembroTop


# herda tudo que a classe Membro tem
class Vip(Membro, MembroTop):
    def __init__(self, nome: str, idade: int, vida: int):
        # chama o construtor da classe pai
        super().__init__(nome, idade, vida)

    def pegar_kit_vip(self) -> None:
        print("Pegando kit vip")
        super().pegar_kit_membro()
