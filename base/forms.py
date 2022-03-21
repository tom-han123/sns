from dataclasses import field, fields
from pyexpat import model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Order,Customer,B_models,Engine

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields='__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        
class CustomerForm(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        exclude=['user']


class BikeForm(ModelForm):
    class Meta:
        model = B_models
        fields='__all__'
        exclude=['type_id']

class EngineForm(ModelForm):
    class Meta:
        model = Engine
        fields='__all__'
        exclude=['model_id']        