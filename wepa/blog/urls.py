from django.urls import path
from . import views


# app = 'blog'

urlpatterns = [
    path('', views.latest_feed, name='homepage'),
    path('post_<int:post_id>/', views.post_details, name='post_details'),
    path('tag_<int:tag_id>/', views.tag_filter, name='tag_filter'),
    # path('year_archive_<int:year>/', views.year_archive, name='year_archive'),
    # path('month_archive_<int:month/', views.month_archive, name='month_archive'),

]
