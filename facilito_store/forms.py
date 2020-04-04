#Este archivo nos permite crear formulario a partir de clases
from django import forms

#La clase debe de heredar de Forms
class RegisterForm(forms.Form):
    username = forms.CharField(required=True,min_length=4,max_length=50)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
