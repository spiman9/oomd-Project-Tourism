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