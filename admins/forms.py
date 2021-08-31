from django import forms
from django.forms import ModelForm

from user.forms import UserRegistrationForm, UserProfileForm

from user.models import User
from products.models import ProductCategory


class AdminUserCreationFrom(UserRegistrationForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'image', 'password1', 'password2')


class AdminUserUpdateForm(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': False}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4', 'readonly': False}))


class AdminCategoryCreate(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', }), required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control py-4',}), required=False)

    class Meta:
        model = ProductCategory
        fields = ('name', 'description')

