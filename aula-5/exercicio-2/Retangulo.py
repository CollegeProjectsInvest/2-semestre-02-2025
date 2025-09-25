class Retangulo:
    def __init__(self, largura: float, altura: float) -> None:
        self.__largura: float = largura
        self.__altura: float = altura

    def calcular_area(self) -> float:
        return self.__largura * self.__altura

    def calcular_perimetro(self) -> float:
        return (self.__largura * 2) + (self.__altura * 2)
