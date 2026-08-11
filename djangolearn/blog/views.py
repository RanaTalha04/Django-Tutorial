from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Welcome to the blog Home Page!")


def about(request):
    return HttpResponse(f"Welcome to Blog about page")
