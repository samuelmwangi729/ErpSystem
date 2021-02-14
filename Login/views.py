from django.shortcuts import render,redirect
from django.contrib import messages
from  django.contrib.auth.models import User,auth

# Create your views here.
def Login(request):
    return render(request,'login.html',{'message':'sam'})
def Loginto(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        #sanitize the input and remove white spaces
        #this is to be done later 
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Wrong Details, Either the email/password is wrong')
            return render(request,'login.html')
    else:
        messages.error(request,'Forbidden!!!Method not Allowed in this route')
        return redirect('login')
def Register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password_confirmation']
        if password != password2:
            message="The Passwords do not match"
            messages.error(request,'The passwords do not match')
            return render(request,'Register.html',{'message':message,'email':email,'first_name': first_name,'last_name':last_name})
        else:
            if User.objects.filter(email=email).exists():
                #then the user exists
                messages.error(request,'User with the email address '+ email +' already exists')
                return render(request,'Register.html',{'message':'','email':email,'first_name': first_name,'last_name':last_name})
            else:
                user= User.objects.create_user(username=email,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                messages.success(request,'user registration successful,Kindly login to Access your Dashboard')
                return redirect('/Account')
        #then the passwords match
    else:
        message="Forbidden!!! The method is not Allowed for this route"
        return render(request,'login.html',{'message':message})
def Logout(request):
    auth.logout(request)
    return redirect('/')