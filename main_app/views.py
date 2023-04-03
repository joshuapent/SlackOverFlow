from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Board, Post, Comment
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class PostCreate(CreateView):
    model = Post
    fields = '__all__'

class PostUpdate(UpdateView):
    model = Post
    fields = '__all__'

class PostDelete(DeleteView):
    model = Post
    success_url = '/boards'

boards = [
    {'board_name': 'global'},
    {'board_name': 'global_errors'},
    {'board_name': 'global_fun'},
    {'board_name': 'classroom'},
    {'board_name': 'classroom_errors'},
    {'board_name': 'classroom_fun'},
]


def home(request):
    return render(request, 'home.html')

def main_forum(request):
    return render(request, 'main_forum.html')

def class_forum(request):
    return render(request, 'class_forum.html')

def boards_index(request):
    return render(request, 'index.html')

def register(request):
    error_message = ''

# def post_detail(request):
