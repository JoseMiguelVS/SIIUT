from django import forms
from django.contrib.auth.forms import AuthenticationForm

input_class = 'border border-gray-400 p-1 rounded-xl mt-2'

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': input_class, 'placeholder': 'Usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': input_class, 'placeholder':'Contraseña'}))