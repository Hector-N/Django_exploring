from django.urls import path
# from .views import home
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('<int:poll_num>/', views.show_poll, name='details'),
    path('<int:poll_num>/vote/', views.vote_poll, name='vote'),
    path('<int:poll_num>/results/', views.show_results, name='results'),
]
