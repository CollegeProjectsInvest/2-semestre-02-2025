numeros: list[int] = [10, 20, 100, 11]

# adiciona um elemento no final da lista
numeros.append(10)
numeros.append(11)
numeros.insert(1, 100)
numeros.remove(100)

# pegando o primeiro elemento da lista
# print(numeros[0])
# print(numeros[1])

# print(numeros)
print(len(numeros))   # tamanho da lista

# percorrer elementos de uma lista
for index, elemento in enumerate(numeros):
    print(f"Elemento: {elemento} está na {index} posição")
    # if elemento % 2 == 0:
    #     print(f"{elemento} é par")

# matriz = [
#     [10, 10, 10],
#     [10, 10, 10]
# ]
