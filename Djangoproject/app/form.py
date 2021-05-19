from django import forms
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = UserRecord
        fields = '__all__'


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['User_Name','Image', 'Caption']
        widgets = {
            'User_Name':forms.HiddenInput()
        }