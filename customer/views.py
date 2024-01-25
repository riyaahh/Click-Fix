from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


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
        

    # ## Validation for first name
    #     if not first_name:
    #         errors['first_name'] = 'First name is required.'

    # ## Validation for last name
    #     if not last_name:
    #         errors['last_name'] = 'Last name is required.'

    ## Validation for Register number
        # if not register_number:
        #     errors['register_number'] = 'Register number is required.'
        # else:
        #     is_used = User.objects.filter(username='register_number').exists()
        #     if is_used:
        #         errors['register_number'] = 'Register number already exits.'

    ## Validation for email
        if not email:
            errors['email'] = 'Email field is required.'
        else:
            is_used = User.objects.filter(email='email').exists()
            if is_used:
                errors['email'] = 'This email is already taken.'

    # ## Validation for department
    #     if not department:
    #         errors['department'] = 'Deaprtment is required.'

    ## Validation for username
        if not username:
            errors['username'] = 'Username field is required.'
        else:
            is_used = User.objects.filter(username='username').exists()
            if is_used:
                errors['username'] = 'This username is already taken.'

    ## Validation for password
        if not password:
            errors['password'] = 'Password is required.'
       

        is_valid = len(errors.keys()) == 0

        if is_valid:

            ## Creating an user

            user = User.objects.create_user(
                # first_name = first_name,
                # last_name = last_name,
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

 



   

    