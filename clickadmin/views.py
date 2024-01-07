from django.shortcuts import render


def registration(request):
    return render(request,"admin/registration.html",context={})
