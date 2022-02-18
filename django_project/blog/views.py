from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse
# we no longer need to import HttpResponse since we're no longer using it

# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html', {'title': 'About'})