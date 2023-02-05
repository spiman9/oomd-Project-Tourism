from django.db import models

# Create your models here.
class contactus(models.Model):
    email=models.EmailField()
    fname=models.TextField()
    lname=models.TextField()
    country=models.TextField()
    description=models.TextField()
    def __str__(self):
        return self.email
class India(models.Model):
    name=models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    numberPerson = models.IntegerField()
    sdate = models.DateField()
    edate = models.DateField()
    acctype = models.CharField(max_length=100)
    queries = models.CharField(max_length=100)

class Dubai1(models.Model):
    name=models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    numberPerson = models.IntegerField()
    sdate = models.DateField()
    edate = models.DateField()
    acctype = models.CharField(max_length=100)
    queries = models.CharField(max_length=100)

class Singapore(models.Model):
    name=models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    numberPerson = models.IntegerField()
    sdate = models.DateField()
    edate = models.DateField()
    acctype = models.CharField(max_length=100)
    queries = models.CharField(max_length=100)

class specialoffer(models.Model):
    fname=models.CharField(max_length=50)
    sname=models.CharField(max_length=50)
    phno=models.IntegerField(max_length=12)
    email=models.EmailField()
    d1=models.DateField()
    d2=models.DateField()
    def __str__(self):
        return self.fname+self.sname


