from django.shortcuts import render



def index(request):
    return render(request,"provider/index.html",context={})
# Create your views here.
