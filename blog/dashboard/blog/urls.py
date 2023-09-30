from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/blog', views.blog, name='blog'),
    path('dashboard/add_group', views.add_group, name='add_group'),
    path('dashboard/delete_group', views.delete_group, name='delete_group'),
    path('dashboard/add_hashtag', views.add_hashtag, name='add_hashtag'),
    path('dashboard/delete_hashtag', views.delete_hashtag, name='delete_hashtag'),
]
