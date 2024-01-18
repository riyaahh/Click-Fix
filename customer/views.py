from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,"provider/index.html",context={})

def register(request):
    return render(request, 'customer\\register.html')

def login(request): 
    if request.method== 'POST':
        username=request.POST('email')
        password=request.POST('password')
        user= authenticate()
        

    return render(request, 'customer\\login.html')



   

    