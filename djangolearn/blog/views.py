from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Welcome to the blog Home Page!")


def about(request):
    return HttpResponse(f"Welcome to Blog about page")

def post_detial(request, post_id):
    return HttpResponse(f"Show blog post {post_id}")

def user_profile(request, username):
    return HttpResponse(f"Profile of User {username}")

def article_by_year(reqeust, year):
    return HttpResponse(f"Articles of year {year}:")

def article_details(reqeust, **kwargs):
    return HttpResponse(f"Details:  {kwargs}")