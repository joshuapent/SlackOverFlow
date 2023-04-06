from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/profile_create/', views.profile_create, name='profile_create'),
    path('forum/', views.main_forum, name='main_forum'),
    path('class-forum/', views.class_forum, name='class_forum'),
    path('boards/', views.board_index, name='index'),
    path('boards/create/', views.BoardCreate.as_view(), name='board_create'),
    path('boards/<int:pk>/delete/', views.BoardDelete.as_view(), name='board_delete'),
    path('boards/<int:board_id>/', views.board_detail, name='board_detail'),
    path('posts/create/', views.PostCreate.as_view(), name='post_create'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('posts/<int:post_id>/comment/', views.comment, name='comment'),
    path('posts/<int:post_id>/comment/<int:comment_id>/edit/', views.comment_edit, name='comment_edit'),
    path('posts/<int:post_id>/comment/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),
    path('posts/<int:pk>/comment/create/', views.CommentCreate.as_view(), name='comment_create'),
    path('posts/<post_id>/comment/<int:pk>/update/', views.CommentUpdate.as_view(), name='comment_update'),
    path('posts/<post_id>/comment/<int:pk>/confirm_delete/', views.CommentDelete.as_view(), name='comment_confirm_delete'),
    # path('posts/<int:post_id>', views.post_detail, name='detail')
    path('user/<int:pk>/', views.UserDetail.as_view(), name='users_detail'),
    path('user/<int:pk>/delete/', views.UserDelete.as_view(), name='users_delete'),
    path('user/<int:user_id>/update/', views.user_edit, name='user_edit'),
    path('user/<int:pk>/update_account/', views.UserUpdate.as_view(), name='user_update'),
    path('user/<int:pk>/profile_update/', views.ProfileUpdate.as_view(), name='profile_update'),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html', success_url = '/accounts/password_change/done/'), name='change_password'),
    path('posts/<int:post_id>/upvote/<int:comment_id>', views.upvote, name='upvote'),
] 