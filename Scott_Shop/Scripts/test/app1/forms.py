from django import forms
from app1.models import user, fooditems, reviews
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class usercreate(forms.ModelForm):
    class Meta:
        model = user
        fields = '__all__'

class fooditemscreate(forms.ModelForm):
    class Meta:
        model = fooditems
        fields = '__all__'  

class reviewscreate(forms.ModelForm):
    class Meta:
        model = reviews
        fields = '__all__'     

class Newuserform(UserCreationForm):
    email = forms.EmailField(required=False)   

    class Meta:
        model = User   
        fields = ("username", "email", "password1", "password2")                     