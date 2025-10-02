from membro import Membro
from vip import Vip


def main() -> None:
    membro_joaquim = Membro()
    membro_joaquim.pegar_kit_membro()

    vip_joaquim = Vip()
    vip_joaquim.nome = "Joaquim"
    vip_joaquim.pegar_kit_membro()
    vip_joaquim.pegar_kit_vip()


if __name__ == '__main__':
    main()
