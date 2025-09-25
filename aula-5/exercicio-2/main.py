from Retangulo import Retangulo


def main() -> None:
    altura: float = float(input("Digite a altura: "))
    largura: float = float(input("Digite a largura: "))
    retangulo = Retangulo(largura, altura)
    print(f"área: {retangulo.calcular_area()}")
    print(f"perímetro: {retangulo.calcular_perimetro()}")


if __name__ == '__main__':
    main()
