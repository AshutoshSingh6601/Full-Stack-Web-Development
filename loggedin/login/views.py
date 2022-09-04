from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('store')
        else:
            return redirect('home')

    return render(request,'home.html')

@login_required(login_url='home')
def store(request):
    return render(request, 'store.html')

def logoutuser(request):
    logout(request)
    return redirect('home')