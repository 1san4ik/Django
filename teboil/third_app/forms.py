from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя * ', widget=forms.TextInput(attrs={'class': 'form-control'}))
    telephone = forms.CharField(label='Телефон * ', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль * ', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля * ', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'telephone', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя * ', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль * ', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
