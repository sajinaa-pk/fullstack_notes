from django import forms  
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

class expform(forms.Form):
  exp=forms.CharField(label="Enter Expense Name")
  amt=forms.CharField(label="Enter Amount")
  
class balform(forms.Form):
  bal=forms.CharField(label="Enter Balance Amount")
  
class UserRegisterForm(UserCreationForm): 
    email = forms.EmailField() 
    phone_no = forms.CharField(max_length = 20) 
    first_name = forms.CharField(max_length = 20) 
    last_name = forms.CharField(max_length = 20) 
    class Meta: 
        model = User 
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']  
 
    