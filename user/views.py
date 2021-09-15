from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
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


class UserRegistrationView(CommonContextMixin, CreateView):

    model = User
    title = 'GeekShop - регистрация'
    template_name = 'user/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('user:login')

    def form_valid(self, form):
        user = form.save()
        if send_verify_email(user):
            success_message = 'Для подтверждения регистрации проверьте почту'
        else:
            success_message = 'Ошибка отправки сообщения'
        messages.success(self.request, success_message)
        return HttpResponseRedirect(self.success_url)


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


def verify(request, email, activation_key):
    try:
        user = User.objects.get(email=email)
        if user.activation_key == activation_key and user.is_activation_key_expires():
            user.is_active = True
            user.save()
            messages.success(request, f'Пользователь {user.username} успешно активирован!')
            return HttpResponseRedirect('user:login')
        elif user.activation_key == activation_key and not user.is_activation_key_expires():
            verify_email_again = reverse('user:another_verify', args=[user.email])
            messages.success(request, f'срок действия ключа для активации пользователя {user.username} истек!',
                             extra_tags=f'{settings.DOMAIN_NAME}{verify_email_again}')
            return HttpResponseRedirect('user:login')
        else:
            messages.error(request, 'Некорректный ключ активации!')
            return HttpResponseRedirect('user:login')
    except Exception as e:
        print(f'error activation user: {e.args}')
        return HttpResponseRedirect(reverse('user:login'))


def send_verify_email(user):
    verify_link = reverse('user:verify', args=[user.email, user.activation_key])
    title = f'Подтверждение учетной записи {user.username} на портале GeekShop'
    message = f'Для подтверждения учетной записи на портале {settings.DOMAIN_NAME} ' \
              f'перейдите по ссылке: \n' \
              f'{settings.DOMAIN_NAME}{verify_link}'
    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def send_verify_email_again(request, email):
    user = User.objects.get(email=email)
    user.generate_activation_key()
    user.save()
    send_verify_email(user)
    messages.success(request, 'Письмо повторно отправлено')
    return HttpResponseRedirect(reverse('user:login'))



