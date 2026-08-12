from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('post_list/', views.post_list, name='post-list')
]