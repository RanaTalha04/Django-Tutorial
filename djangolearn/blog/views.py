from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def about(request):
    return HttpResponse(f"Welcome to Blog about page")

def home(request):
    return render(request, "blog/post_list.html")