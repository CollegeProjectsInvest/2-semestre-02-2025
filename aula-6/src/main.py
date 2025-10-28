from membro import Membro
from vip import Vip


def main() -> None:
    membro_joaquim = Membro("Marcos", 23 + 1, 100)
    membro_joaquim.pegar_kit_membro()

    vip_joaquim = Vip("Joaquim", 25, 100)
    vip_joaquim.nome = "Joaquim"
    vip_joaquim.pegar_kit_membro()
    vip_joaquim.pegar_kit_vip()


if __name__ == '__main__':
    main()
