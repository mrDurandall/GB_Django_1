from django import forms
from django.forms import ModelForm

from user.forms import UserRegistrationForm, UserProfileForm

from user.models import User
from products.models import ProductCategory, Product


class AdminUserCreationFrom(UserRegistrationForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'image', 'password1', 'password2')


class AdminUserUpdateForm(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': False}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4', 'readonly': False}))


class AdminCategoryCreate(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                         'placeholder': 'Введите название категории',
                                                         }), required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control py-4',
                                                               'placeholder': 'Введите описание категории',
                                                               }), required=False)

    class Meta:
        model = ProductCategory
        fields = ('name', 'description', 'is_active')


class AdminProductCreateUpdate(ModelForm):
    categories = ProductCategory.objects.all()
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                         'placeholder': 'Введите название продукта',
                                                         }), required=True)
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control form-control-lg',
                                                           }), required=False)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control py-4',
                                                               'placeholder': 'Введите описание продукта',
                                                               }), required=False)
    price = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                             'placeholder': 'Введите цену продукта',
                                                             }), required=True)
    quantity = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                                'placeholder': 'Введите количество продукта на складе',
                                                                }), required=True)
    category = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-select form-control',
                                                                 'placeholder': 'Выберите категорию продукта',
                                                                 }), required=True,
                                      queryset=ProductCategory.objects.all(), )

    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'price', 'quantity', 'category', 'is_active')

