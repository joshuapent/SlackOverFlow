from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/register/', views.register, name='register'),
    path('forum/', views.main_forum, name='main_forum'),
    path('class-forum/', views.class_forum, name='class_forum'),
    path('boards/', views.boards_index, name='index'),
    path('posts/create/', views.PostCreate.as_view(), name='posts_create'),
    path('posts/<int:perskey>/update/', views.PostUpdate.as_view(), name='posts_update'),
    path('posts/<int:perskey>/delete/', views.PostDelete.as_view(), name='posts_delete'),
    # path('posts/<int:post_id>', views.post_detail, name='detail')
]