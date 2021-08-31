from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from admins.forms import AdminUserCreationFrom, AdminUserUpdateForm
from user.models import User


def index(request):
    context = {
        'title': 'GeekShop - Админка: Главная',
    }
    return render(request, 'admins/index.html', context)


def users(request):
    context = {
        'title': 'GeekShop - Админка: пользователи',
        'users': User.objects.all(),
    }
    return render(request, 'admins/admin-users-read.html', context)


def user_create(request):
    if request.method == 'POST':
        form = AdminUserCreationFrom(files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:users'))
        else:
            print(form.errors)
    else:
        form = AdminUserCreationFrom()
    context = {
        'title': 'GeekShop - Админка: создание пользователя',
        'form': form,
    }
    return render(request, 'admins/admin-users-create.html', context)


def user_update(request, id):
    selected_user = User.objects.get(id=id)
    if request.method == 'POST':
        form = AdminUserUpdateForm(instance=selected_user, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:users'))
    else:
        form = AdminUserUpdateForm(instance=selected_user, )

    context = {
        'title': 'GeekShop - Админка: редактирование пользователя',
        'form': form,
        'selected_user': selected_user,
    }

    return render(request, 'admins/admin-users-update-delete.html', context)


def user_delete(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admins:users'))


def user_restore(request, id):
    user = User.objects.get(id=id)
    user.is_active = True
    user.save()
    return HttpResponseRedirect(reverse('admins:users'))


def categories(request):
    context = {
        'title': 'GeekShop - Админка: категории',
    }
    return render(request, 'admins/admin-categories-read.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Админка: продукты',
    }
    return render(request, 'admins/admin-products-read.html', context)

