from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,"provider/index.html",context={})

def register(request):
    return render(request, 'customer\\register.html')


   

    