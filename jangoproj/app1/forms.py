
from django import forms
from models import Usermodel1


class SignUpform(forms.ModelForm):
    class Meta:
        model = Usermodel1
        fields=['name','email','username','password']


class loginform(forms.ModelForm):
    class Meta:
        model = Usermodel1
        fields=['username','password']
