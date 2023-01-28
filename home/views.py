from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
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