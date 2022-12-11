from collections import UserDict, UserList
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required

def Home(request):
    return render(request, 'application/index.html', {})


def Register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        name = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pword')
        password2=request.POST.get('pword2')

        new_user = User.objects.create_user(name, email, password) 
        new_user.first_name = fname
        new_user.last_name = lname
        new_user.password =password2

        new_user.save()
        return redirect('login-page')

        

    return render(request, 'application/register.html',{})

def Login(request): 
     if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('pword')

        User = authenticate(request, username=name, password=password)
        if User is not None:
            login(request, User)
            return redirect('home-page')
        else:
            return HttpResponse('Error, user does not exist')

     return render(request, 'application/Login.html',{})

def logoutuser(request):
        logout(request)
        return redirect('login-page')

def Aboutus(request):
    return render(request, "application/Aboutus.html", {})

def resetpassword(request):
    return render(request, "application/resetpassword.html", {})

def Faq(request):
    return render(request, "application/Faq.html", {})


def contactus(request):
    return render(request, "application/Contactus.html", {})

def privacypolicy(request):
    return render(request, "application/privacy_policy_preview.html", {})

def tcpreview(request):
    return render(request, "application/TC_preview.html")
