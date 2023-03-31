from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Poster(User):
#     def __init__(self, )

class Board(models.Model):
    board_name = models.CharField(max_length=50)

class Post(models.Model):
    upvotes = models.IntegerField()
    resolved = models.BooleanField(default=False)
    text = models.TextField(max_length=1000)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    upvotes = models.IntegerField()
    text = models.TextField(max_length=1000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)