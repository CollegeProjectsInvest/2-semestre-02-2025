# idade: int = 17
# nome: str = "Marcos"
# cidade: str = "Cuiabá"
#
# if idade >= 18 and nome == "Marcos":
#     print("Marcos maior de idade")
#     if cidade == "Cuiabá":
#         print("ele é de cuiabá")


# if False:
#     print("verdade")
# else:
#     print("falsa")

# nota: int = 5
#
# if nota < 5:
#     print("Reprovador")
# elif 6 > nota <= 8:
#     print("Precisa melhorar")
# else:
#     print("Aprovado!")

# Loop

# for i in range(0, 5):
#     print(i)
#
# for letra in "Python":
#     print(letra)
#
# for elemento in [5, 6, 10, 1]:
#     print(elemento)

# while True:
#     print("Infinito")

contador: int = 0
while contador < 10:
    print(contador)
    contador += 1

    if contador == 5:
        break   # para o loop

print("Saiu do loop")
