from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


class todoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todolist', null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


""" creating a model to contain all the todos  """


class todoItems(models.Model):
    todolist = models.ForeignKey(todoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=250)
    complete = models.BooleanField(default=False)
    dateTime = datetime.datetime.now()

    def __str__(self):
        """ returning a string representing the models here """
        return self.text
