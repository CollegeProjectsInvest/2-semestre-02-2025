from pessoa import Pessoa


# ponto de partida
# tudo será executado a partir daqui
def main() -> None:
    pessoa_objeto_marcos = Pessoa(
        "Marcos",
        "marcos@mail.com",
        23 + 1
    )  # objeto da classe Pessoa
    pessoa_objeto_marcos.cadastrar()

    pessoa_objeto_joao = Pessoa(
        "João",
        "joao@mail.com",
        23
    )
    pessoa_objeto_joao.cadastrar()


if __name__ == '__main__':
    main()
