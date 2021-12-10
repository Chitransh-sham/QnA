from django.db import models
from django.contrib.auth.models import User,auth
from phone_field import PhoneField
from datetime import datetime




# Create your models here.

class Registration(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    contactNO=PhoneField()
    image=models.ImageField(upload_to="mypic",null=True,blank=True)
    profession= models.CharField(max_length=150,null=True,blank=True)
    
    
    def __str__(self):
        return self.user.first_name
 
class contactus(models.Model):
    UserID=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    message=models.CharField(max_length=1000)
    def __str__(self):
        return self.UserID

class postdata(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    reg=models.ForeignKey(Registration,on_delete=models.CASCADE)
    question=models.CharField(max_length=300,blank=True)
    pimg=models.ImageField(upload_to="mypics",blank=True)

    
    def __str__(self):
        return self.user.first_name

 

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
 