import controller.tarefas_controller as controller

while True:
    print('1 - Cadastrar tarefa\n2 - Listar tarefas\n3 - Finalizar')

    escolha = input('Escolha uma opção: ')
    if escolha == '1':
        controller.adicionar_tarefa()
    elif escolha == '2':
        controller.exibir_tarefas()
    elif escolha == '3':
        print('Obrigado!')
        break