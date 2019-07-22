from django.shortcuts import render


def home(request):
    return render(request, 'story/home.html')


def about(request):
    return render(request, 'story/about.html')
