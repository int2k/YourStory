from django.urls import path
from .views import home, about
urlpatterns = [
    path('', home, name='story-home'),
    path('about/', about, name='story-about'),
]
