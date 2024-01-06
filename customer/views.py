from django.shortcuts import HttpResponse
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world")

def about(request):
    return HttpResponse("About page")
    
def Customer(request):
    return HttpResponse("Customer page")

def provider(request):
    return HttpResponse("Provider page")

def conatact(request):
    return HttpResponse("Contact page")


