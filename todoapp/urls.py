# todoapp/urls.py
from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),  # /login/ にログインページを設定
    path('todos/', views.todo_list, name='todo_list'),
]
