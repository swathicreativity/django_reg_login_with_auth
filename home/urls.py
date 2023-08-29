from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),        
    path("signin",views.signin,name="signin"),
    path('signup_page',views.signup_page,name='signup_page'),
    path('signin_verification',views.signin_verification,name="signin_verification"),
    path('otp_verification',views.otp_verification,name="otp_verification"),
    path("secure",views.secure,name="secure"),    
    path('logout_page',views.logout_page,name='logout_page'),
]
