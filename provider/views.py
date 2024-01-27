from django.shortcuts import render
from django.http import HttpResponse
# from provider.models import 


def provider_dashboard(request):
    return render(request,"provider/dashboard.html",context={})
def bookings(request):
    return render(request,"provider/bookings.html",context={})
def bookform(request):
    return render(request,"provider/bookform.html",context={})
def prof(request):
    return render(request,"provider/prof.html",context={})
def profform(request):
    return render(request,"provider/profform.html",context={})
