from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='post-list'),
    path('about/', views.about, name='blog-about'),
]