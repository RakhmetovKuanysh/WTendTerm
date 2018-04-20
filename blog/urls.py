from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('new_blog/', views.new_blog, name='new_blog'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('delete_blog/<int:blog_id>', views.delete_blog, 
        name='delete_blog'),
    path('detail_blog/<int:blog_id>', views.detail_blog, 
        name='detail_blog'),
    path('edit_blog/<int:blog_id>', views.edit_blog, 
        name='edit_blog'),
]