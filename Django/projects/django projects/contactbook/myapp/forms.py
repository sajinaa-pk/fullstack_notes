from django import forms
from myapp.models import contact
class phoneForm(forms.ModelForm):
    class Meta:
        model=contact
        fields="__all__"

class nameform(forms.Form):
    oname=forms.CharField(max_length=100)
    nname=forms.CharField(max_length=100) 


class phoneform(forms.Form):
    name=forms.CharField(max_length=100)
    newnumber=forms.CharField(max_length=20)           