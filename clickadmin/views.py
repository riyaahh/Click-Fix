from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login

def index(request):
    return render(request,"home/index.html")

def about(request):
    return render(request,"home/about.html")

def contact(request):
    return render(request,"home/contact.html",context={})

def service(request):
    return render(request,"home/service.html",context={})



def signin(request):

    if request.method == "POST":
        email=request.POST.get('email')
        pasword=request.POST.get('password')

        user=authenticate(request, username=email,password=pasword)
        if user is not None:
            
            if user.is_superuser:
                login(request,user)
                request.session['admin_id']=user.id
                return redirect("index")
            elif user.is_staff:
                login(request,user)
                request.session['admin_id']=user.id
                return redirect("index")
            else:
                login(request,user)
                request.session['admin_id']=user.id
                return redirect("user")
        else:
            msg='invalid details'
            return render(request,'customer\login.html',{'msg':msg})
    else:
            return render(request,'customer\login.html')
        


def register(request):
    errors = {}
    if request.method == 'POST':

        firstname = request.POST['firstName'].strip()
        lastname = request.POST['secondName'].strip()
        email = request.POST['email'].strip()
        gender = request.POST['Gender'].strip()
        password = request.POST['password'].strip()
        phonenumber=request.POST['phoneNo'].strip()

        new_user=User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=email,password=password,is_active=True)
        userDetails.objects.create(user=new_user,phone_number=phonenumber,gender=gender)
        return redirect('login')
    else:
        return render(request, 'customer\Register.html')



def admin_dashboard(request):
    return render(request,'clickadmin/dashboard.html')
