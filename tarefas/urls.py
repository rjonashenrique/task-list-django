from django.urls import path
from tarefas.views import home, task_details


# * Separando os urls entre os aplicativos = mais organizado
# * E assim copiamos a estrutura principal do urls.py original
urlpatterns = [
    path('', home, name='home'),
    path('tarefa-detalhes/<int:id>', task_details, name='task-details'),
]
