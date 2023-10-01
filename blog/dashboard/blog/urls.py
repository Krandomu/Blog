from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/blog/', views.blog, name='blog'),
    path('dashboard/blog/add_categorie/', views.add_categorie, name='add_categorie'),
    path('dashboard/blog/delete_categorie/', views.delete_categorie, name='delete_categorie'),
    path('dashboard/blog/categorie/<int:categorie_id>/', views.blog_categorie, name='blog-categorie'),
    path('dashboard/blog/categorie/add_subcategorie/', views.add_subcategorie, name='add-subcategorie'),
    path('dashboard/blog/categorie/delete_subcategorie/', views.delete_subcategorie, name='delete-subcategorie'),
    path('dashboard/blog/categorie/add_post/', views.add_post, name='add-post'),
    path('dashboard/blog/categorie/delete_post/', views.delete_post, name='delete-post'),
    path('dashboard/blog/categorie/post/<int:post_id>/', views.post, name='post'),

]
