from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='product-list'),
    path('product/', views.product, name='shop-product'),
]