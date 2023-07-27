# from django.shortcuts import render

# # Create your views here.

from django.http import HttpResponse


# Function-based view
def index(request):
    return HttpResponse("Hello, world. You're at the posts index.")
