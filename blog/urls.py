from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),  # Matching url path to url function home()
]