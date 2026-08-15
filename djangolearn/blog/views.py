from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

class User: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

def home(request):
    context = {
        "name": "Muhammad Talha",
        "age": 22,
        "skills": ["Python", "Gen AI", "SQA"],
        "user": User("Muhammad Ali", 24),
        "blog": {
            "title": "First Django Blog",
            "content": "This is the first django blog",
            "created_at": datetime(2026, 8, 15, 11, 5)
        },
        "updated_content": "no",
        "bold_value": "<b>This is bold value</b>",
        "viewers": 100,
        "subscription": 27,
        "comment_count": 5,
        
    }
    return render(request, "blog/home.html", context)

    


def about(request):
    return HttpResponse(f"Welcome to Blog about page")
