from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('forum/', views.main_forum, name='main_forum'),
    path('class-forum/', views.class_forum, name='class_forum'),
    path('boards/', views.boards_index, name='index'),
    # path('posts/<int:post_id>', views.post_detail, name='detail')
]