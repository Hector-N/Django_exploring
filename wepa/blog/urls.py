from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.feed, name='homepage'),
    path('post_<int:post_id>/', views.post_details, name='post_details'),
    path('post_<int:post_id>/add_comment/', views.add_comment),
    path('tag_<int:tag_id>/', views.tag_filter, name='tag_filter'),
    path('year<int:year>/', views.feed, name='year_archive'),
    path('year<int:year>/month<int:month>/', views.feed, name='month_archive'),
]
