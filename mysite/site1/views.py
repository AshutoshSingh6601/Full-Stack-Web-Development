from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("you are in hame")

def about(request):
    return HttpResponse("you are in about page")

def contact(request):
    return HttpResponse("you are in contact page")