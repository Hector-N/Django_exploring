from django.urls import path

from . import views


urlpatterns = [
    path('index.html', views.output, name='index'),
    path('addTask/', views.add_task, name='add_task_x'),
    path('deleteTask/<int:task_id>/', views.delete_task, name='delete_task_x')
]
