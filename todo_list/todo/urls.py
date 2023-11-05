from django.urls import path
from django.shortcuts import render
from .views import list_todo, mark_task_done, done, create_task, delete_task

urlpatterns = [
    path('', list_todo, name='list_todo'),
    path('done/', done, name='done'),
    path('mark_task_done/<int:task_id>/', mark_task_done, name='mark_task_done'),
    path('add/', create_task, name='create_task'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
]
