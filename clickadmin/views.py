from django.shortcuts import render


def registration(request):
    return render(request,"customer/register.html",context={})
