from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home')
    path('boards/', views.boards_index, name='index')
]