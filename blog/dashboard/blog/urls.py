from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/blog/', views.blog, name='blog'),
    path('dashboard/blog/add_category/', views.add_category, name='add_category'),
    path('dashboard/blog/delete_category/', views.delete_category, name='delete_category'),
    path('dashboard/blog/category/<int:category_id>/', views.blog_category, name='blog-category'),
    path('dashboard/blog/category/add_subcategory/', views.add_subcategory, name='add-subcategory'),
    path('dashboard/blog/category/delete_subcategory/', views.delete_subcategory, name='delete-subcategory'),
    path('dashboard/blog/category/add_post/', views.add_post, name='add-post'),
    path('dashboard/blog/category/delete_post/', views.delete_post, name='delete-post'),
    path('dashboard/blog/category/post/<int:post_id>/', views.post, name='post'),
    path('update_or_delete_section/', views.update_or_delete_section, name='update_or_delete_section'),

]
