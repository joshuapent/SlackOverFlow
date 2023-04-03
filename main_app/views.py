from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Board, Post, Comment
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class BoardCreate(CreateView):
    model = Board
    fields = ['board_name']

class BoardDelete(DeleteView):
    model = Board
    success_url = '/boards'

class PostCreate(CreateView):
    model = Post
    fields = ['text']

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
    return redirect('login')

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', {
        'post': post
    })

def board_detail(request, board_id):
    board = Board.objects.get(id=board_id)
    return render(request, 'board_detail.html', {
        'board': board
    })

def main_forum(request):
    return render(request, 'main_forum.html')

def class_forum(request):
    return render(request, 'class_forum.html')

def board_index(request):
    return render(request, 'index.html')

def register(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - quit slacking off'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/register.html', context)

# def post_detail(request):
