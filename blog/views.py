from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse  # <-- Will handle the traffic from the homepage of the blog

def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')