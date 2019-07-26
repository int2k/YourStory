from django.urls import path
from .views import (
    PostListView,
    AboutPageView,
    PostCreateView,
    PostDetailView
)

urlpatterns = [
    path('', PostListView.as_view(), name='story-home'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', AboutPageView.as_view(), name='story-about'),
]
