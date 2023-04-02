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

# def post_detail(request):
