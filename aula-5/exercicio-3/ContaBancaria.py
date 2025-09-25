import random


class ContaBancaria:
    def __init__(self) -> None:
        self.__numero_conta: int = random.randint(1000, 10000)
        self.__saldo: float = 0

    def visualizar_saldo(self) -> None:
        print(f"Seu saldo: R${self.__saldo}")

    def depositar(self, value: float) -> None:
        self.__saldo += value

    def sacar(self, value: float) -> None:
        self.__saldo -= value
