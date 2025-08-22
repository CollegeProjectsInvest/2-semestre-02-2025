nome_variavel: int = 10
nome_variavel = 1  # valor da variavel alterada
print("Valor da variavel: ", nome_variavel)
nome_variavel = "Marcos"  # Tipagem fraca
print(f"Valor da variavel: {nome_variavel}")

altura: float = 1.80
nome: str = "Marcos"
idade: int = 23 + 1
maior_idade: bool = True  # False

print(f"Nome: {nome}")

peso: int = 100
peso += 50 // 2  # peso = peso + 50
print(f"Peso: {peso}")

x: int = 10
y: int = 5
print(x == y)  # bool
print(x > y)
print(x <= y)
print(x != y)

print(x == 1 or x == 10)  # True
print(x == 0 and y == 5)  # False
print(not x == 10)  # False
