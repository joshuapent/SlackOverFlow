from django.contrib import admin
from .models import Board, Post, Comment, Profile, Upvotes

# Register your models here.
admin.site.register(Board)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Upvotes)