from django.contrib import admin
from .models import Priority,TaskType,Task
# Register your models here.
class PriorityAdmin(admin.ModelAdmin):
    ...
class TaskTypeAdmin(admin.ModelAdmin):
    ...
class TaskAdmin(admin.ModelAdmin):
    ...

admin.site.register(Priority,PriorityAdmin)
admin.site.register(TaskType,TaskTypeAdmin)
admin.site.register(Task,TaskAdmin)