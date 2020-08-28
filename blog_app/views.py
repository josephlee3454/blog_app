from django.shortcuts import render
from django.views.generic import TemplateView, ListView ,DetailView
from .models import BlogApp
# Create your views here.
class HomePageView(ListView):
  template_name = 'home.html'
  model = BlogApp
class PostDetailView(DetailView):
  template_name = 'post-detail.html'
  model = BlogApp