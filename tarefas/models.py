from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# ^ Criamos primeiro as tabelas/models fortes (Que não depende de outras tabelas)
# * E depois criamos as fracas
class Priority (models.Model):
    #* Chave primaria - AutoField == AutoIncrement
    id_priority = models.AutoField(primary_key=True)
    #* CharField == Varchar(150)
    name = models.CharField(max_length=50)

class TaskType (models.Model):
    id_task_type = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)

# ^ Agora faremos a entidade/tabela/model fraca
# ^ Onde terá as chaves estrangeiras de priority e task_type
class Task (models.Model):
    id_task = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    # * Chaves estrangeiras
    id_priority = models.ForeignKey(Priority, null=True, blank=True, on_delete=models.SET_NULL)

    id_task_type = models.ForeignKey(TaskType, null=True, blank=True, on_delete=models.SET_NULL)
    
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
