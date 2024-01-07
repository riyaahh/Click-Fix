from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,"provider/index.html",context={})

def chumma(request):
    return render(request, 'chummareg.html')
