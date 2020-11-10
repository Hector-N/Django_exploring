from django.urls import path
from . import views


urlpatterns = [
    path('index.html', views.joke_page, name='index'),
]
