usuarios = []
usuario = {}

while True:
    nome = input("Digite seu nome: ")
    email = input("Digite sua email: ")
    idade = int(input("Digite sua idade: "))

    usuario["nome"] = nome
    usuario["email"] = email
    usuario["idade"] = idade

    usuarios.append(usuario)

    sair = input("Quer sair? S/N")
    if sair == "S":
        break

print(usuarios)
