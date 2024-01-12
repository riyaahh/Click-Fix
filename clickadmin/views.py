from django.shortcuts import render
from django.http import HttpResponse






def index(request):
    return render(request,"clickadmin/index.html",context={})
def about(request):
    return render(request,"clickadmin/about.html",context={})
def contact(request):
    return render(request,"clickadmin/contact.html",context={})
def service(request):
    return render(request,"clickadmin/service.html",context={})
def login(request):
    return render(request,"customer/login.html",context={})
# Create your views here.

