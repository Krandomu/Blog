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
    path('dashboard/blog/category/post/update_or_delete_section/', views.update_or_delete_section, name='update_or_delete_section'),
    path('dashboard/blog/category/post/add/title/<int:post_id>/', views.add_title, name='add_title'),
    path('dashboard/blog/category/post/add/text/<int:post_id>/', views.add_text, name='add_text'),
    path('dashboard/blog/category/post/add/code/<int:post_id>/', views.add_code, name='add_code'),
    path('dashboard/blog/category/post/add/image/<int:post_id>/', views.add_image, name='add_image'),
    path('dashboard/blog/category/post/add/file/<int:post_id>/', views.add_file, name='add_file'),

]