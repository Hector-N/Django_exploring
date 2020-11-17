from django.urls import path
# from .views import home
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('poll<int:poll_num>/', views.show_poll, name='details'),
    path('poll<int:poll_num>/vote/', views.vote_poll, name='vote'),
]
