from django.urls import path
from .views import home


app_name = 'polls'

urlpatterns = [
    path('', home, name='homepage'),
]
