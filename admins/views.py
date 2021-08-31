from django.shortcuts import render


def index(request):
    context = {
        'title': 'GeekShop - Админка: Главная',
    }
    return render(request, 'admins/index.html', context)


def users(request):
    context = {
        'title': 'GeekShop - Админка: пользователи',
    }
    return render(request, 'admins/admin-users-read.html', context)


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

