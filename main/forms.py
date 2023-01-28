from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserUserForm(UserCreationForm):
    username = forms.CharField(min_length=2, max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Логин'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Почта'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Повтор пароля'}))
