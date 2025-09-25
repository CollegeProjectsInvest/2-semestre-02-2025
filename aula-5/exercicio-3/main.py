from Pessoa import Pessoa


def main() -> None:
    nome = input("Digite seu nome: ")
    pessoa = Pessoa(nome)

    while True:
        option: int = int(input("""Digite uma opção:
        [0] Visualizar Saldo
        [1] Depositar
        [2] Sacar
        [-1] Sair
        """))

        if option == 0:
            pessoa.conta_bancaria.visualizar_saldo()
        elif option == 1:
            value = float(input("Digite um valor: "))
            pessoa.conta_bancaria.depositar(value)
        elif option == 2:
            value = float(input("Digite um valor: "))
            pessoa.conta_bancaria.sacar(value)
        elif option == -1:
            print("Volte sempre")
            break
        else:
            print("Opção inválida")


if __name__ == '__main__':
    main()
