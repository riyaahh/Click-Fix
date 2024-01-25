from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm

from .models import *
# from .forms import OrderForm
# from .filters import OrderFilter


def index(request):
    return render(request,"provider/index.html",context={})

def register(request):
    
    context={}

    return render(request, 'customer\\register.html',context)

def user(request):
    return render(request,'customer\\user.html')

def login(request): 
    context={}
    return render(request, 'customer\\login.html',context)
    # if request.method== 'POST':
    #     username=request.POST('email')
    #     password=request.POST('password')
    #     user= authenticate()
        

 



   

    