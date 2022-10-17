from django.views.generic import ListView, DetailView, TemplateView
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = "posts.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class BlogHome(TemplateView):
    model = Post
    template_name = "home.html"