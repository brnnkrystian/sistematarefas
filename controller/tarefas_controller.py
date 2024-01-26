import models.tarefas_model as model
import view.tarefas_view as view

def adicionar_tarefa():
    tarefa = view.nova_tarefa()
    model.adicionar_tarefa(tarefa)

def exibir_tarefas():
    tarefas = model.get_tarefas()
    view.exibir_tarefas(tarefas)