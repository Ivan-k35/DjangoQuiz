from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        min_length=2, max_length=50, widget=forms.TextInput(
            attrs={'placeholder': 'Логин', 'class': 'form-control'}
        )
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Почта', 'class': 'form-control'}
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Пароль', 'class': 'form-control'}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Повтор пароля', 'class': 'form-control'}
        )
    )


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        min_length=2, max_length=50, widget=forms.TextInput(
            attrs={'placeholder': 'Логин', 'class': 'form-control'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Пароль', 'class': 'form-control'}
        )
    )
