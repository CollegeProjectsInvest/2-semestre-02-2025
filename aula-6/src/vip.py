from membro import Membro, MembroTop


# herda tudo que a classe Membro tem
class Vip(Membro, MembroTop):
    def pegar_kit_vip(self) -> None:
        print("Pegando kit vip")
