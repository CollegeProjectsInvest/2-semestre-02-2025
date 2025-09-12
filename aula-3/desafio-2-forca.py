palavra_secreta = input("Digite a palavra secreta: ")
print(palavra_secreta)

palavra_tentativa = ""

for letra in palavra_secreta:
    palavra_tentativa += "_"
print(f"{len(palavra_secreta)} letras\n")
print(palavra_tentativa)

print("""
  /-------
  |      |
  |     (_)
  |
  | 
__|__
""")

while True:
    letra_tentativa = input("Digite uma letra: ")
    for index, letra in enumerate(palavra_secreta):
        if letra == letra_tentativa:
            # replace
            palavra_tentativa = palavra_tentativa[:index] + letra_tentativa + palavra_tentativa[index+1:]
    print(palavra_tentativa)
