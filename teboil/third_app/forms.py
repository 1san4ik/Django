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





# class LoginForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'].label = 'Логин'
#         self.fields['password'].label = 'Пароль'
#
#     def clean(self):
#         username = self.cleaned_data['username']
#         password = self.cleaned_data['password']
#         if not User.objects.filter(username=username).exists():
#             raise forms.ValidationError('Неверный Логин или Пароль')
#         user = User.objects.filter(username=username).first()
#         if User:
#             if not user.check_password(password):
#                 raise forms.ValidationError('Неверный Логин или Пароль')
#         return self.cleaned_data
#
#     class Meta:
#         model = User
#         fields = ['username', 'password']
