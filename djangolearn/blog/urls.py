from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:post_id>/', views.post_detial, name='post-detail'),
    path('user/<str:username>/', views.user_profile, name='user-profile'),
    path('article/<int:year>/<int:month>/<int:day>/', views.article_details, name="article-detail"),
    
    re_path(r'^article/(?P<year>[0-9]{4})/$', views.article_by_year, name='article-by-year')
]