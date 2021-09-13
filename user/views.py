from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from user.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from basket.models import Basket, User
from common.views import CommonContextMixin


class UserLoginView(CommonContextMixin, LoginView):
    template_name = 'user/login.html'
    form_class = UserLoginForm
    title = 'GeekShop - авторизация'


class UserLogoutView(LogoutView):
    pass


class UserRegistrationView(CommonContextMixin, SuccessMessageMixin, CreateView):

    model = User
    title = 'GeekShop - регистрация'
    template_name = 'user/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('user:login')
    success_message = 'Вы зарегистрированы!'


class ProfileView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = User
    template_name = 'user/profile.html'
    form_class = UserProfileForm
    success_message = 'Данные изменены!'

    def get_success_url(self):
        return reverse_lazy('user:profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['baskets'] = Basket.objects.filter(user=self.object)
        context['title'] = 'GeekShop - Профиль'
        return context


