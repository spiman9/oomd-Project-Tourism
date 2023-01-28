from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def home(request):
    return render(request ,"main.html")
def contactus(request):
    return render(request,"contactus.html")

def contactussub(request):
    if request.method=="POST":
        print("hihihdaics")
        email=request.POST["email"]
        fname=request.POST["firstname"]
        lname=request.POST["lastname"]
        country=request.POST["country"]
        sub=request.POST["subject"]
        msg=str(sub)
        htmlgen = '<p>Message from <strong>'+fname+' '+lname+' from '+country+ ' </strong>'+msg+'</p>'
        
        send_mail('Feedback ,',msg,email,[settings.EMAIL_HOST_USER],fail_silently=False,html_message=htmlgen)
        messages.success(request,"Successfull Messag send")
    else:
        print("else")
    return render(request,"contactus.html")

