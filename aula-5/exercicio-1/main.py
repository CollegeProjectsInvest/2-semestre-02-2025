from pessoa import Pesssoa


def main() -> None:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    pessoa = Pesssoa(nome, idade)
    pessoa.apresentar()


if __name__ == '__main__':
    main()
