# todoapp/views.py

from django.shortcuts import render, redirect
from .models import TodoItem
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TodoItemForm 


@login_required
def todo_list(request):
    todos = TodoItem.objects.filter(user=request.user)
    user_name = request.user.username  # ユーザ名を取得
    return render(request, 'todoapp/todo_list.html', {'todos': todos, 'user_name': user_name})

@login_required
def add_todo(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            # フォームが有効な場合、ToDoアイテムを保存
            todo_item = form.save(commit=False)
            todo_item.user = request.user
            todo_item.save()
            return redirect('todo_list')  # ToDoリスト画面にリダイレクト
    else:
        form = TodoItemForm()
    return render(request, 'todoapp/add_todo.html', {'form': form})

