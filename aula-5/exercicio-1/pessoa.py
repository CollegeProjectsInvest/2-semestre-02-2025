class Pesssoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def apresentar(self) -> None:
        print(f"Olá {self.nome}, você tem {self.idade} anos.")
