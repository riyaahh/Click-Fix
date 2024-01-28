from django.shortcuts import render
from django.http import HttpResponse
# from provider.models import 



# def index(request):
#     return render(request,"provider/index.html",context={})
# def about(request):
#     return render(request,"provider/about.html",context={})
# def contact(request):
#     return render(request,"provider/contact.html",context={})
# def service(request):
#     return render(request,"provider/service.html",context={})
# # Create your views here.


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
def history(request):
    return render (request,"provider/history.html",context={})
    
