from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class HoodForm(forms.ModelForm):
    class Meta:
        model = Hood
        fields = ['name', 'location','image',]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user',]


class BusinessForm(forms.ModelForm):
    class Meta:
        model  = Business
        fields = ['business_name','hood','address','owner','category']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description']