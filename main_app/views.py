from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Board, Post, Comment, UserProfile
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy


# Create your views here.

class BoardCreate(CreateView):
    model = Board
    fields = ['board_name']

class BoardDelete(DeleteView):
    model = Board
    success_url = '/boards'

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'text', 'board']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'text']

class PostDelete(DeleteView):
    model = Post
    success_url = '/boards'

class CommentCreate(CreateView):
    model = Comment
    fields = ['text', 'post']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CommentUpdate(UpdateView):
    model = Comment
    fields = ['text']

class CommentDelete(DeleteView):
    model = Comment
    success_url = '/boards'

class UserDetail(DetailView):
    model = User

class UserUpdate(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    success_url = '/boards'

class UserDelete(DeleteView):
    model = User
    success_url = '/'

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
    comments = Comment.objects.all()
    return render(request, 'post-detail/post_detail.html', {
        'post': post,
        'comments': comments
    })

def board_detail(request, board_id):
    board = Board.objects.get(id=board_id)
    posts = Post.objects.all()
    return render(request, 'board_detail.html', {
        'board': board,
        'posts': posts
    })

def main_forum(request):
    return render(request, 'main_forum.html')

def class_forum(request):

    return render(request, 'class_forum.html')

def board_index(request):
    posts = Post.objects.all()
    boards = Board.objects.all()
    return render(request, 'index.html', {
        'posts': posts,
        'boards': boards
    })

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
