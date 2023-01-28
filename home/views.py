from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
<<<<<<< HEAD
from .models import India , Singapore , Dubai

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
        obj = Dubai.objects.create(name = name , email = email , numberPerson = numberperson , sdate = sdate , edate = edate , acctype = atype ,  queries = comment)
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
=======
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

>>>>>>> 9904c6b71080c14e90173b9382835fa786a8bb68
