from django import forms
from django.http import request
from .models import Profile
from django.contrib.auth.models import User


class UpdateForm(forms.ModelForm):
  
    class Meta:
    
        model = User
        fields = ['username']



  
class ProfileForm(forms.ModelForm):
  
    class Meta:
        model = Profile
        fields = ['user','fullname', 'photo']
        widgets ={
    'user':forms.Select(attrs={ 'class': 'form-control'}),
       'fullname':forms.TextInput(attrs={ 'class': 'form-control'})}
