from django.urls import path, include
from . import views


urlpatterns = [
    path('dashboard/', views.index, name='dashboard'),
    path('' , include('dashboard.blog.urls')), 
]
