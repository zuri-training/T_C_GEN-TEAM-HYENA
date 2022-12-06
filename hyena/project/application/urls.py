from django.urls import path
from .views import Homepage, Signup, Signin,  logoutuser

urlpatterns = [
    
    path('home/', Homepage, name="home-page"),
    path('signup/', Signup, name="signup-page"),
    path('signin/', Signin, name="signin-page"),
    path('logout/', logoutuser, name="logout")
]