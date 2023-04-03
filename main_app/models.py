from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Poster(User):
#     def __init__(self, )



class Board(models.Model):
    board_name = models.CharField(max_length=50)

    def __str__ (self):
        return f"{self.board_name}"

class Post(models.Model):
    upvotes = models.IntegerField(default=0)
    resolved = models.BooleanField(default=False)
    title = models.TextField(max_length=100)
    text = models.TextField(max_length=1000)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    upvotes = models.IntegerField(default=0)
    text = models.TextField(max_length=1000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)