from django.shortcuts import render,redirect

from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User,auth
from .models import contactus as CU
# Create your views here.
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from .models import India , Singapore , Dubai1

# Create your views here.
def home(request):
    return render(request ,"main.html")

def india(request):
    if request.method == "POST":
        name= request.POST['name']
        email = request.POST['email']
        numberperson = request.POST['numPerson']
        sdate = request.POST['sdate']
        edate = request.POST['edate']
        atype = request.POST['atype']
        comment = request.POST['comments']
        # Create a object of India
        obj = India.objects.create(name = name , email = email , numberPerson = numberperson , sdate = sdate , edate = edate , acctype = atype ,  queries = comment)
        obj.save()
        return redirect("/")
    return render(request , "joinusIndia.html")

def dubai(request):
    if request.method == "POST":
        name= request.POST['name']
        email = request.POST['email']
        numberperson = request.POST['numPerson']
        sdate = request.POST['sdate']
        edate = request.POST['edate']
        atype = request.POST['atype']
        comment = request.POST['comments']
        # Create a object of India
        obj = Dubai1.objects.create(name = name , email = email , numberPerson = numberperson , sdate = sdate , edate = edate , acctype = atype ,  queries = comment)
        obj.save()
        return redirect("/")
    return render(request , "joinusDubai.html")


def singapore(request):
    if request.method == "POST":
        name= request.POST['name']
        email = request.POST['email']
        numberperson = request.POST['numPerson']
        sdate = request.POST['sdate']
        edate = request.POST['edate']
        atype = request.POST['atype']
        comment = request.POST['comments']
        # Create a object of India
        obj = Singapore.objects.create(name = name , email = email , numberPerson = numberperson , sdate = sdate , edate = edate , acctype = atype ,  queries = comment)
        obj.save()
        return redirect("/")
    return render(request , "joinusSingapore.html")

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
        b=CU(email=email,fname=fname,lname=lname,country=country,description=sub)
        b.save()
        messages.success(request,"Successfull Messag send")
    else:
        print("else")
    return render(request,"contactus.html")

def register(request):
    return render(request,"register.html")
def login(request):
    return render(request,"login.html")

def filllogin(request):
    if request.method=="POST":
        user=auth.authenticate(username=request.POST['uname'],password=request.POST["psw"])
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            print("User not present")
            return render(request,"login.html")
    else:
        return render(request,"login.html")

def fillregister(request):
    if request.method=="POST":
        if User.objects.filter(username=request.POST["uname"]).exists():
            messages.error(request,"Username already exist")
            return render(request,"register.html")
        if User.objects.filter(email=request.POST["email"]).exists():
            messages.error(request,"Email already exist")
            return render(request,"register.html")
        if(request.POST["psw1"]!=request.POST["psw2"]):
            messages.error(request,"Pls enter the correct password")
            return render(request,"register.html")
        
        x=User.objects.create_user(username=request.POST["uname"],email=request.POST["email"],first_name=request.POST["fname"],last_name=request.POST["lname"],password=request.POST["psw1"])
        return render(request,"main.html")
def logout(request):
    auth.logout(request)
    return redirect("/")