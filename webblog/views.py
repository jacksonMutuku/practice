from django.shortcuts import render
from django.views.generic import ListView, DetailView
from.models import Post

class HomePageView(ListView):
    model = Post
    template_name = 'webblog/home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'webblog/post_detail.html'


# Create your views here.
