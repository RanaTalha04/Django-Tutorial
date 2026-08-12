from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def product(request):
    return HttpResponse(f"Welcome to Shop Product page")

def home(request):
    return render(request, "shop/product_list.html")