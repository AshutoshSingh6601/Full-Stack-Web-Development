from multiprocessing import context
import django
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.http import HttpResponse

from .models import Login, Register

# Create your views here.


def register_form(request):
    # return HttpResponse('This is the Resgister Page')
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        address=request.POST.get('address')
        Register(username=username, password=password, address=address).save()
    return render(request,'register.html')

def login_form(request):
    # return HttpResponse('This is the login page')
    # username_register=Register.objects.all()
    # password_register=Register.objects.all()
    if request.method=='POST':

        username=request.POST.get('username')
        user_data=Register.objects.get(username=username)
        password=request.POST.get('password')
        pass_data=Register.objects.get(password=password)        

        Login(username=user_data, password=pass_data).save()
    # context={
    #     'user_data':username_register,
    #     'pass_data':password_register,
    # }
    return render(request,'login.html',context)


def store(request):
    return HttpResponse('This is the store Page')