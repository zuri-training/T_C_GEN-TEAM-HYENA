from django.urls import path
from .views import index, Register, Login,  logoutuser, Aboutus, resetpassword, Faq, contactus, privacypolicypreview,tcpreview
from .views import tcgen,tcmodal,privacypolicy,tcmodal2,tcmodal3, popup, privacymodal1, privacymodal3, privacymodal2,tc_condition
from .views import ready, ready2
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
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
    path('tcmodal2/',tcmodal2, name="tcmodal2"),
    path('tcmodal3/', tcmodal3, name="tcmodal3"),
    path('popup/', popup, name="popup"),
    path('privacymodal1/', privacymodal1, name="privacymodal1"),
    path('privacymodal3/', privacymodal3, name="privacymodal3"),
    path('privacymodal2/', privacymodal2, name="privacymodal2"),
    path('tc_condition/', tc_condition, name="tc_condition"),
    path('ready/', ready, name="ready"),
    path('ready2/', ready2, name="ready2"),

    ]