from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from .models import userDetails


def customer_dashboard(request):
    return render(request,"customer/dashboard.html")

def UserData(request):
    return render(request,"customer/UserData.html",context={})



   

    