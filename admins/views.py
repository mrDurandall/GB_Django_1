from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from admins.forms import AdminUserCreationFrom, AdminUserUpdateForm, AdminCategoryCreate
from user.models import User
from products.models import ProductCategory


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
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'admins/admin-categories-read.html', context)


def category_add(request):
    if request.method == 'POST':
        form = AdminCategoryCreate(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:categories'))
        else:
            print(form.errors)
    else:
        form = AdminCategoryCreate()
    context = {
        'title': 'GeekShop - Админка: добавление категории',
        'form': form,
    }
    return render(request, 'admins/admin-category-create.html', context)


def category_edit(request, id):
    selected_category = ProductCategory.objects.get(id=id)
    if request.method == 'POST':
        form = AdminCategoryCreate(instance=selected_category, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:categories'))
        else:
            print(form.errors)
    else:
        form = AdminCategoryCreate(instance=selected_category, )
    context = {
        'title': 'GeekShop - Админка: Редактирование категории',
        'form': form,
        'selected_category': selected_category,
    }
    return render(request, 'admins/admin-category-edit.html', context)


def category_delete(request, id):
    selected_category = ProductCategory.objects.get(id=id)
    selected_category.delete()
    return HttpResponseRedirect(reverse('admins:categories'))


def products(request):
    context = {
        'title': 'GeekShop - Админка: продукты',
    }
    return render(request, 'admins/admin-products-read.html', context)

