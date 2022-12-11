from django.urls import path
from .views import index, Register, Login,  logoutuser, Aboutus, resetpassword, Faq, contactus, privacypolicypreview,tcpreview
from .views import tcgen,tcmodal,privacypolicy
urlpatterns = [
    
    path('index/', index, name="home-page"),
    path('register/', Register, name="register-page"),
    path('login/', Login, name="login-page"),
    path('logout/', logoutuser, name="logout"),
    path('Aboutus/', Aboutus, name="Aboutus" ),
    path('resetpassword/', resetpassword, name= "resetpassword"),
    path('Faq/',Faq,name="Faq"),
    path('contactus/', contactus, name="contactus"),
    path('privacypolicypreview/', privacypolicypreview, name="privacy_policy_preview"),
    path('TC_preview/',tcpreview, name="TC_preview"),
    path('tcgen/',tcgen,name="tcgen"),
    path('tcmodal/',tcmodal,name="tcmodal"),
    path('privacypolicy/',privacypolicy, name="privacypolicy"),
    

    
    ]