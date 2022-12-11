from django.urls import path
from .views import Privacypolicy, Homepage, Register, Login,  logoutuser, Aboutus, resetpassword

urlpatterns = [
    
    path('home/', Homepage, name="home-page"),
    path('register/', Register, name="register-page"),
    path('login/', Login, name="login-page"),
    path('logout/', logoutuser, name="logout"),
    path('Aboutus/', Aboutus, name="Aboutus" ),
    path('resetpassword/', resetpassword, name= "resetpassword"),
    path('privacypolicy/', Privacypolicy , name= "privacypolicy"),

]