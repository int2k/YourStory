from django.urls import path
from .views import (
    PostListView,
    AboutPageView
)

urlpatterns = [
    path('', PostListView.as_view(), name='story-home'),
    path('about/', AboutPageView.as_view(), name='story-about'),
]
