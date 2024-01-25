from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     return render(request,"provider/index.html",context={})
# def about(request):
#     return render(request,"provider/about.html",context={})
# def contact(request):
#     return render(request,"provider/contact.html",context={})
# def service(request):
#     return render(request,"provider/service.html",context={})
# # Create your views here.
def bookings(request):
    return render(request,"provider/bookings.html",context={})
def bookform(request):
    return render(request,"provider/bookform.html",context={})