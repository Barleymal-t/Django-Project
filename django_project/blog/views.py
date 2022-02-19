from re import template
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
# from django.http import HttpResponse
# we no longer need to import HttpResponse since we're no longer using it

# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html', context)

class PostListview(ListView):
    model = Post
    template_name ='blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

def about(request):
    return render(request,'blog/about.html', {'title': 'About'})