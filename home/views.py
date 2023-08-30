# from django.shortcuts import render

# # Create your views here.
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
import random
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request,"home.html") 

def signin(request):
    return render(request,"signin.html") 

def signup_page(request):
    if request.method=='POST':
        username=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        request.session["username"]=username
        request.session["password"]=password1
        request.session["email"]=email

        if password1!=password2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            encryptedpassword=make_password(request.session['password'])
            nameuser=User(username=request.session['username'],email=request.session['email'],password=encryptedpassword)
            nameuser.save()
            messages.info(request,'Registered in successfully...')
            return redirect('signin')
    return render (request,'signup.html')

def signin_verification(request):
     if request.method=="POST":
        email=request.POST["email"]
        request.session["email"]=email
        if User.objects.filter(email=email).exists():
                send_otp(request)
                return render(request,'otp.html',{"email":email})
        else:
                messages.info(request,"email doesnot exist")
                return redirect('http://localhost:8000/')
     else:
                return HttpResponse("No Page")

def send_otp(request):
    s=""
    for x in range(0,6):
        s+=str(random.randint(0,9))
    request.session["otp"]=s
    send_mail("otp for sign up",s,'onlinetrainingnumber1@gmail.com',[request.session['email']],fail_silently=False)
    return render(request,"otp.html")

def  otp_verification(request):
    if  request.method=='POST':
        otp_=request.POST.get("otp")
    if otp_ == request.session["otp"]:
        return render(request,'secure.html')
    else:
        messages.error(request,"otp doesn't match")
        return render(request,'otp.html')

def logout_page(request):
    logout(request)
    return redirect('http://localhost:8000/')

def secure(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('secure')
    return render(request,'http://localhost:8000/')
