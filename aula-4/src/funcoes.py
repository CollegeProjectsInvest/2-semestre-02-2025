def capturar_valor(mensagem: str) -> None:
    """Essa função captura valores"""
    valor = input(mensagem)
    print(valor)


def soma_valores(*numeros: float) -> int:
    # print(sum(numeros))
    # print(len(numeros))  # tamanho da estrutura
    return sum(numeros)


# capturar_valor("Digite seu nome: ")
# capturar_valor("Digite sua idade: ")

soma = soma_valores(10, 20, 123, 123, 3123, 123)

print(soma_valores(1231230, 123123))
