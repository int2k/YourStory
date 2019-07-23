from .models import Post
from django.views.generic import (
    ListView,
    TemplateView
)


class PostListView(ListView):
    model = Post
    template_name = 'story/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class AboutPageView(TemplateView):
    template_name = 'story/about.html'
