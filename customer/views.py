from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,"provider/index.html",context={})

def register(request):
    return render(request, 'customer\\register.html')

def user(request):
    return render(request,'customer\\user.html')

def login(request): 
    return render(request, 'customer\\login.html')
    # if request.method== 'POST':
    #     username=request.POST('email')
    #     password=request.POST('password')
    #     user= authenticate()
        

 



   

    