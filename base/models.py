from ast import mod
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Types(models.Model):
    name=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class B_models(models.Model):
    type_id=models.ForeignKey(Types,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    description=models.TextField(null=True)
    base_prize=models.IntegerField(default=0)
    prize=models.IntegerField(default=0)
    quantity=models.IntegerField(default=0)
    image=models.ImageField(default="s1000rr.jpg",null=True,blank=True)
    

    def __str__(self):
        return self.name

class Engine(models.Model):
    model_id=models.ForeignKey(B_models,on_delete=models.CASCADE)
    engine_type=models.CharField(max_length=200,null=True)
    bore_stroke=models.CharField(max_length=200,null=True)
    capacity=models.CharField(max_length=200,null=True)
    rated_output=models.CharField(max_length=200,null=True)
    torque=models.CharField(max_length=200,null=True)
    compression=models.CharField(max_length=200,null=True)
    mixture_control=models.CharField(max_length=200,null=True)
    emission_control=models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.model_id)

class Staff(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True) 
    email=models.CharField(max_length=200,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name



class Customer(models.Model):
    name=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True) 
    email=models.CharField(max_length=200,null=True)
    image=models.ImageField(default="user.png",null=True,blank=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name  

class Order(models.Model):
    STATUS=(
        ('Pending','Pending'),
        ('Out of delivery','Out of delivery'),
        ('Delivered','Delivered'),
    )

    model_id=models.ForeignKey(B_models,null=True,on_delete=models.SET_NULL)
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    quantity=models.IntegerField(default=0)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=200,null=True,choices=STATUS)

    def __str__(self):
        return str(self.id)