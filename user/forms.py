from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

from user.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                             'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4',
                                                                 'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                             'placeholder': 'Введите имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4',
                                                           'placeholder': 'Введите email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                               'placeholder': 'Введите ваше имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                              'placeholder': 'Введите вашу фамилию'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4',
                                                                  'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4',
                                                                  'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        if len(data) < 2:
            raise forms.ValidationError('Имя коротковато!')

        return data

