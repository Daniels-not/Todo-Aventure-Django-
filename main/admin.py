from django.contrib import admin
from .models import todoList, todoItems

# Register your models here.
admin.site.register(todoList)
admin.site.register(todoItems)