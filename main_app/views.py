from django.shortcuts import render

# Create your views here.
# def signup()

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

# def post_detail(request):
