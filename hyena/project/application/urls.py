from django.urls import path
from .views import Home, Register, Login,  logoutuser, Aboutus, resetpassword, Faq, Contactus

urlpatterns = [
    
    path('index/', Home, name="home-page"),
    path('register/', Register, name="register-page"),
    path('login/', Login, name="login-page"),
    path('logout/', logoutuser, name="logout"),
    path('Aboutus/', Aboutus, name="Aboutus" ),
    path('resetpassword/', resetpassword, name= "resetpassword"),
    path('Faq/',Faq,name="Faq"),
    path('contactus/', Contactus, name="contactus"),
    

]