from django.urls import path
from .views import BlogListView, BlogDetailView, BlogHome

urlpatterns = [
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("posts/", BlogListView.as_view(), name="posts"),
    path("", BlogHome.as_view(), name="home"),
]