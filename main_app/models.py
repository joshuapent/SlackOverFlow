from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    instructor = models.BooleanField(default=False)
    star_dev = models.BooleanField(default=False)
    profile_pic = models.TextField(default='https://i.imgur.com/TaUnF6t.png')

    def __str__ (self):
        return f"{self.user}"


class Board(models.Model):
    board_name = models.CharField(max_length=50)

    def __str__ (self):
        return f"{self.board_name}"
    
    def get_absolute_url (self):
        return reverse('board_detail', kwargs={'board_id': self.id})

class Post(models.Model):
    resolved = models.BooleanField(default=False)
    title = models.TextField(max_length=100)
    text = models.TextField(max_length=1000)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def upvote_count(self):
        return self.upvotes.count()

    def __str__ (self):
        return f'{self.user.name}: ({self.title})'
    
    def get_absolute_url (self):
        return reverse('post_detail', kwargs={'post_id': self.id})

class Comment(models.Model):
    text = models.TextField(max_length=1000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


    def __str__ (self):
        return f'{self.user}, {self.post.title}'
    
    def get_absolute_url (self):
        return reverse('post_detail', kwargs={'post_id': self.post.id})

class Upvotes(models.Model):
    post = models.OneToOneField(Post, related_name='upvotes', on_delete=models.CASCADE)
    users = models.ManyToManyField(User)

    def __str__ (self):
        return f"Like connected to: {self.post.title}"
