from django.shortcuts import render
from utils.tarefas.factory import make_task

# Create your views here.
# * Criando a view de home
# * View = função que vai mostrar a visualização/visual da página
# ! request = pedido
# ! O cliente (PC do usuário) pediu a página 'home' esse pedido chega como 'request' 
def home(request):
    
    # * Retorna = Volta com uma resposta (response)
    
    return render(request, 'tarefas/pages/index.html', 
                  context={
                     'tasks' : [make_task() for _ in range(10)],
                  })

"""
* Com o faker (Depois muda pro banco de dados)
^ O make_task() gera uma tarefa falsa (para testes)
^ E passamos para o 'task_details.html' a informação chamada 'task' onde dentro tem a tarefa fictícia
* Mas é uma tarefa SÓ, já que é ela em detalhes
* Diferente do home que são 10, aqui é uma só.
^ Lá no .html usamos esse 'task' para mostrar CADA INFORMAÇÃO
"""
def task_details(request, id):
    return render(request, 'tarefas/pages/task_details.html',
                  context={
                      'task' : make_task(),
                  })