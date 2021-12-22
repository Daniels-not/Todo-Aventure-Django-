from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import todoList, todoItems
from .form import CreateNewTodo


# Create your views here.

# index page


def index(response):
    user = response.user
    return render(response, 'index.html', {'user': user})


# page to list all our todos


def todos(response):
    return render(response, 'todos.html')


# base template


def base(response, id):
    item = todoList.objects.get(id=id)
    return render(response, 'base.html', {"item": item})


# items page


def items(response, id):
    item = todoList.objects.get(id=id)

    if response.method == 'POST':

        print(response.POST)

        if response.POST.get('save'):

            for item in item.todoitems_set.all():

                if response.POST.get("c" + str(item.id)) == 'clicked':

                    item.complete = True

                else:

                    item.complete = False

                item.save()

        elif response.POST.get('newItem'):

            item.todoitems_set.create(text=response.POST.get('newType'), complete=False)

        else:

            print("invalid")

    return render(response, 'items.html', {"item": item})


# Method to create a new item in the todo list


def create(response):
    if response.method == 'POST':

        form = CreateNewTodo(response.POST)

        if form.is_valid():
            name = form.cleaned_data['name']

            todo = todoList(name=name)

            todo.save()

            response.user.todolis_set.add(todo)

        return HttpResponseRedirect("/%i" % todo.id)

    else:

        form = CreateNewTodo()

    return render(response, 'create.html', {"form": form})



