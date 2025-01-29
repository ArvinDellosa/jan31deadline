from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Post


class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class RegisterPageView(TemplateView):
    template_name = 'app/register.html'

class LoginPageView(TemplateView):
    template_name = 'app/login.html'

class BlogListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'app/blog_list.html'
