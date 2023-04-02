from django.shortcuts import render

# Create your views here.
# def signup()

def home(request):
    return render(request, 'home.html')

# def post_detail(request):
