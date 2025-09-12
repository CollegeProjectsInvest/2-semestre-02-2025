lista_tarefas: list[str] = []


def adicionar_tarefa() -> None:
    # adicionar
    print("=== Adicionando Tarefa ===")
    nome_tarefa: str = input("Digite o nome da tarefa: ")
    lista_tarefas.append(nome_tarefa)


def remover_tarefa() -> None:
    # remover
    print("=== Removendo Tarefa ===")
    nome_tarefa: str = input("Digite o nome da tarefa para remover: ")
    lista_tarefas.remove(nome_tarefa)


def listar_tarefas() -> None:
    # listar
    print("=== Listando Tarefas ===")
    for index, tarefa in enumerate(lista_tarefas):
        print(f"[{index}]: {tarefa}")


while True:
    operacao: int = int(input("""=== Gerenciamento Tarefas ===
    [0]: Adicionar Tarefa
    [1]: Remover Tarefa
    [2]: Listar Tarefas
    [3]: Sair
    """))

    if operacao == 0:
        adicionar_tarefa()
    elif operacao == 1:
        remover_tarefa()
    elif operacao == 2:
        listar_tarefas()
    elif operacao == 3:
        print("Volte sempre!")
        break
    else:
        print("Operação inválida")
