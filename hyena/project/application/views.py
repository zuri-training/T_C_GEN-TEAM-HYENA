from collections import UserDict, UserList
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm  
from .forms import CustomUserCreationForm 
from django.contrib.auth import forms 
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

# def Register(request):  
#     if request.POST == 'POST':  
#         form = CustomUserCreationForm(request.POST)  
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Your account has been created ! You are now able to log in')
#             return redirect('login-page')
            
#     else:  
#         form = CustomUserCreationForm()  
#     context = {  
#         'form':form  
#     }  
#     return render(request, 'application/register.html', context)



def Login(request): 
     if request.method == 'POST':
        name = request.POST['uname']
        password = request.POST['pword']

        user = authenticate(request, username=name, password=password,)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
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

def setting(request):
    return render(request, 'application/dashboard_setting.html', {})

@login_required
def dashboard(request):
    return render(request, 'application/dashboard.html', {})

def privacygen(request):
    return render (request, "application/privacygen.html",{})