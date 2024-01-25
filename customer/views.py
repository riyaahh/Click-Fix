from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

def user(request):
    return render(request,"customer/user.html",context={})


def login(request):
    if request.method == "POST":
        email=request.POST.get('email')
        request.POST['register_number']
        pasword=request.POST['password']

        user=authenticate(request, email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect("/index")
        


def register(request):

 

    errors = {}
    if request.method == 'POST':

       
        fullname = request.POST['fullname'].strip()
        email = request.POST['email'].strip()
      
        username = request.POST['username'].strip()
        password = request.POST['password'].strip()
        phonenumber=request.POST['phonenumber'].strip()

    
    context={}

    return render(request, 'customer\\register.html',context)

def user(request):
    return render(request,'customer\\user.html')

def login(request): 
    context={}
    return render(request, 'customer\\login.html',context)
   
        

   
    if not email:
            errors['email'] = 'Email field is required.'
    else:
            is_used = User.objects.filter(email='email').exists()
    if is_used:
                errors['email'] = 'This email is already taken.'

   
                errors['username'] = 'Username field is required.'
    else:
            is_used = User.objects.filter(username='username').exists()
    if is_used:
                errors['username'] = 'This username is already taken.'

 
    if not password:
            errors['password'] = 'Password is required.'
       

            is_valid = len(errors.keys()) == 0

    if is_valid:

          user = User.objects.create_user(
                
                username = username,
                email = email,
                password = password,
            )
            
    user.save()
    return redirect("/home")
    
    context = {
        'errors' : errors
            }

    return render (request, "register.html", context)

 



   

    