from django.shortcuts import render # Default import
# My imports
from django.http import HttpResponse   

def home(request):
    return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return HttpResponse('<h1>Blog About</h1>')