# todoapp/views.py

from django.shortcuts import render, redirect
from .models import TodoItem
from django.contrib.auth.decorators import login_required

@login_required
def todo_list(request):
    todos = TodoItem.objects.filter(user=request.user)
    return render(request, 'todoapp/todo_list.html', {'todos': todos})
