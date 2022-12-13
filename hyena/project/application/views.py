from collections import UserDict, UserList
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
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

        User = authenticate(request, username=name, password=password,)
        if User is not None:
            login(request, User)
            return redirect('tcgen')
        else:
            return HttpResponse('Error, user does not exist')

     return render(request, 'application/login.html',{})

def logoutuser(request):
        logout(request)
        return render(request, 'application/index.html', {})

def Aboutus(request):
    return render(request, "application/Aboutus.html", {})

def resetpassword(request):
    return render(request, "application/resetpassword.html", {})

def Faq(request):
    return render(request, "application/Faq.html", {})


def contactus(request):
    return render(request, "application/Contactus.html", {})

def privacypolicypreview(request):
    return render(request, "application/privacy_policy_preview.html", {})


def tcpreview(request):
    return render(request, "application/TC_preview.html", {})
    
@login_required
def tcgen(request):
    return render (request,  "application/TC_Generator_page.html", {})


def tcmodal(request):
    return render(request, "application/TC_Modal_page_1.html", {}) 


def privacypolicy(request):
    return render (request, "application/privacypolicy.html",{})


def tcmodal2(request):
    return render(request, "application/TC_Modal_page_2.html", {})


def tcmodal3(request):
    return render (request, "application/TC_Modal_page_3.html", {})


def popup(request):
    return render (request, "application/popup _page.html", {})


def privacymodal1(request):
    return render (request, "application/privacy_modal1_page.html", {}) 


def privacymodal3(request):
    return render (request, "application/privacy_modal3_page.html", {}) 


def privacymodal2(request):
    return render (request, "application/privacy_modal2_page.html", {})        


def tc_condition(request):
    return render(request, "application/Termscondition.html", {})

def ready(request):
    return render(request, 'application/ready.html',{})

def ready2(request):
    return render(request, 'application/ready2.html',{})
