from django import forms
from django.contrib.auth.models import User
from paste.models import Category, Page, UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password')
