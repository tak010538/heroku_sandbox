# todoapp/urls.py
from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(
        redirect_authenticated_user=True,
        template_name='registration/login.html'
    ), name='login'),  # /login/ にログインページを設定
    path('todos/', views.todo_list, name='todo_list'),
    path('add-todo/', views.add_todo, name='add_todo'),  
]