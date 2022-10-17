from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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

class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body", "cover"]

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body", "cover"]

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")

