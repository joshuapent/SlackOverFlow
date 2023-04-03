from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/register/', views.register, name='register'),
    path('forum/', views.main_forum, name='main_forum'),
    path('class-forum/', views.class_forum, name='class_forum'),
    path('boards/', views.board_index, name='index'),
    path('boards/create/', views.BoardCreate.as_view(), name='board_create'),
    path('boards/delete/', views.BoardDelete.as_view(), name='board_delete'),
    path('boards/<int:board_id>/', views.board_detail, name='board_detail'),
    path('posts/create/', views.PostCreate.as_view(), name='post_create'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/<int:perskey>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('posts/<int:perskey>/delete/', views.PostDelete.as_view(), name='post_delete'),
    # path('posts/<int:post_id>', views.post_detail, name='detail')
    path('user/<int:pk>', views.UserDetail.as_view(), name='users_detail'),
    path('user/<int:pk>/update', views.UserUpdate.as_view(), name='users_update'),
    path('user/<int:pk>/delete', views.UserDelete.as_view(), name='users_delete'),
]