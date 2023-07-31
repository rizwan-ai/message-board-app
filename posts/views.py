# from django.shortcuts import render

# # Create your views here.

# from django.http import HttpResponse


# # Function-based view
# def index(request):
#     return HttpResponse("Hello, world. You're at the posts index.")

# ...............

# from django.views.generic import TemplateView

# class HomePageView(TemplateView):
#     template_name = "index.html"

# ----------

from django.views.generic import ListView
from .models import Post


class ListPageView(ListView):
    model = Post
    template_name = "index.html"
