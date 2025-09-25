from ContaBancaria import ContaBancaria


class Pessoa:
    def __init__(self, nome: str) -> None:
        self.__nome = nome
        self.conta_bancaria = ContaBancaria()
