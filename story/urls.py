from django.urls import path
from .views import (
    PostListView,
    AboutPageView,
    PostCreateView
)

urlpatterns = [
    path('', PostListView.as_view(), name='story-home'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', AboutPageView.as_view(), name='story-about'),
]
