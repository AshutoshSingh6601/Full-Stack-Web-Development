from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("we are in home")

def about(request):
    return HttpResponse("we are in about")

def contact(request):
    return HttpResponse("we are in contact")