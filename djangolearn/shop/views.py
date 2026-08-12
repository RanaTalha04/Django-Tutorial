from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Welcome to the Shop Home Page!")


def product(request):
    return HttpResponse(f"Welcome to Shop Product page")

def product_list(request):
    return render(request, "shop/product_list.html")