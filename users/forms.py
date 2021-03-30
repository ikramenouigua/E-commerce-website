from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

 
CHOICES = [('1', 'Seller'), ('2', 'Buyer'),('3', 'Both')]
class LoginForm(forms.Form):
     
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=256)
    password = forms.CharField()
    password2 = forms.CharField()
   
    trade= forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields= ['username','email','password1','password2']


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=255, required=True,
                            widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

