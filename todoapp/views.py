# todoapp/views.py

from django.shortcuts import render, redirect
from .models import TodoItem
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse


@login_required
def todo_list(request):
    todos = TodoItem.objects.filter(user=request.user)
    user_name = request.user.username  # ユーザ名を取得
    return render(request, 'todoapp/todo_list.html', {'todos': todos, 'user_name': user_name})

def add_todo(request):
    if request.method == 'POST':
        task = request.POST['task']
        TodoItem.objects.create(user=request.user, task=task, completed=False)
    return HttpResponseRedirect(reverse('todo_list'))
