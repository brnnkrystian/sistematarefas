def nova_tarefa():
    return input("Digite uma nova tarefa: ")

def exibir_tarefas(tarefas):
    for tarefa in tarefas:
        print("##########")
        print(tarefa)
        print("##########")