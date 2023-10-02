from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>', views.subcategories, name='subcategories'),
    path('categories/subcategory/<int:subcategory_id>', views.posts, name='posts'),
]
