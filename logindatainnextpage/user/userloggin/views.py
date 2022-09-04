from django.shortcuts import render
from .models import Loggin
from datetime import datetime
from django.contrib.auth.hashers import make_password
# Create your views here.

def home(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=make_password(request.POST.get('password'))
        date_time=datetime.now()
        user=Loggin(username=username,email=email,password=password,date_time=date_time)
        user.save()
        user_info=Loggin.objects.get(id=user.id)
        context={
            'user_info':user_info,
        }
        return render(request,'show.html',context)
    return render(request,'home.html')

def show(request):
    return render(request,'show.html')