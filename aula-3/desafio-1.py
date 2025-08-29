import random

numero_aleatorio: int = random.randint(0, 101)
chances_total: int = 5
chances: int = 1

while True:
    escolha: int = int(input("Digite um número: "))

    if escolha == numero_aleatorio:
        print("Você acertou!")
        break
    elif escolha > numero_aleatorio:
        print("O número é menor.")
    else:
        print("O número é maior")

    if chances >= chances_total:
        print("Perdeu!")
        break

    chances += 1
