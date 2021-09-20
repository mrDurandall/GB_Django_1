from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from user.models import User, UserProfile


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

    def save(self):
        user = super(UserRegistrationForm, self).save()

        user.is_active = False
        user.generate_activation_key()
        user.save()
        return user


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4', 'readonly': True}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email')


class UserProfileEditForm(forms.ModelForm):

    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOISES = (
        (MALE, 'М'),
        (FEMALE, 'Ж'),
    )

    tagline = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                            'placeholder': 'Введите тэги'}),
                              required=False)
    aboutme = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control py-4',
                                                           'placeholder': 'Сведения о себе',
                                                           }), required=False)
    gender = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-select form-control',
                                                          }),
                               required=False,
                               choices=GENDER_CHOISES)

    class Meta:
        model = UserProfile
        fields = ('gender', 'tagline', 'aboutme', )
