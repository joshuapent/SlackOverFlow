from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Board, Post, Comment, Profile, Upvote
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm
from main_app.forms import ProfileForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy


# Create your views here.

# CBVs start here
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

class UserDelete(DeleteView):
    model = User
    success_url = '/boards'

class UserUpdate(UpdateView):
    model = User
    fields = ['username', 'email']
    success_url = '/boards'


class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['profile_pic']
    success_url = '/boards'
# CBVs end

def upvote(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    # post = Post.objects.get(id=post_id)
    # user = User.objects.get(id=request.session.user)
    upvote = Upvote.objects.create(comment=comment, user=request.user)
    upvote.isclicked = True
    upvote.save()
    return redirect(f'/posts/{post_id}')
    # else:
    #     upvote = Upvote.objects.filter(comment=comment, user=request.user).delete()
    #     return redirect(f'/posts/{post_id}')


def user_edit(request, user_id):
    user = User.objects.get(id=user_id)
    profile = Profile.objects.get(id=user_id)
    return render (request, 'auth/user_form.html', {
        'user': user,
        'profile': profile
    })

def home(request):
    return redirect('login')

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.all()
    return render(request, 'post-detail/post_detail.html', {
        'post': post,
        'comments': comments
    })

def comment(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.all()
    return render(request, 'post-detail/comment_create.html', {
        'post': post,
        'comments': comments
    })

def comment_delete(request, post_id, comment_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.all()
    comment = Comment.objects.get(id=comment_id)
    return render(request, 'post-detail/comment_confirm_delete.html', {
        'post': post,
        'comments': comments,
        'selected_comment': comment
    })

def comment_edit(request, post_id, comment_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.all()
    comment = Comment.objects.get(id=comment_id)
    return render(request, 'post-detail/comment_edit.html', {
        'post': post,
        'comments': comments,
        'selected_comment': comment
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
    user = request.user
    posts = Post.objects.all()
    boards = Board.objects.all()
    return render(request, 'index.html', {
        'posts': posts,
        'boards': boards,
        'user': user
    })

def register(request):
    error_message = ''
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile_create')
        else:
            error_message = 'Invalid sign up - quit slacking off'
    form = ProfileForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/register.html', context)

def profile_create(request):
    newUser = User.objects.last()
    newProfile = Profile.objects.create(user=newUser)
    if newProfile:
        newProfile.save()
        return redirect('index')
    
