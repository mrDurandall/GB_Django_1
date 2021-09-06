from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from admins.forms import AdminUserCreationFrom,\
                        AdminUserUpdateForm, \
                        AdminCategoryCreate, \
                        AdminProductCreateUpdate
from user.models import User
from products.models import ProductCategory, Product


# Главная админки
# @user_passes_test(lambda u: u.is_staff)
# def index(request):
#     context = {
#         'title': 'GeekShop - Админка: Главная',
#     }
#     return render(request, 'admins/index.html', context)


class AdminIndexView(TemplateView):

    template_name = 'admins/index.html'

    def get_context_data(self, **kwargs):
        context = super(AdminIndexView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Админка: Главная'
        return context
    
    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminIndexView, self).dispatch(request, *args, **kwargs)


# Список пользователей
# @user_passes_test(lambda u: u.is_staff)
# def users(request):
#     context = {
#         'title': 'GeekShop - Админка: пользователи',
#         'users': User.objects.all(),
#     }
#     return render(request, 'admins/admin-users-read.html', context)

class UsersListView(ListView):

    template_name = 'admins/admin-users-read.html'
    model = User

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UsersListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Админка: пользователи'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UsersListView, self).dispatch(request, *args, *kwargs)


# Добавление пользователей
# @user_passes_test(lambda u: u.is_staff)
# def user_create(request):
#     if request.method == 'POST':
#         form = AdminUserCreationFrom(files=request.FILES, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:users'))
#         else:
#             print(form.errors)
#     else:
#         form = AdminUserCreationFrom()
#     context = {
#         'title': 'GeekShop - Админка: создание пользователя',
#         'form': form,
#     }
#     return render(request, 'admins/admin-users-create.html', context)

class UserCreateView(CreateView):

    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = AdminUserCreationFrom
    success_url = reverse_lazy('admins:users')

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Админка: создание пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)


# Изменение пользователя
# @user_passes_test(lambda u: u.is_staff)
# def user_update(request, id):
#     selected_user = User.objects.get(id=id)
#     if request.method == 'POST':
#         form = AdminUserUpdateForm(instance=selected_user, files=request.FILES, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:users'))
#     else:
#         form = AdminUserUpdateForm(instance=selected_user, )
#
#     context = {
#         'title': 'GeekShop - Админка: редактирование пользователя',
#         'form': form,
#         'selected_user': selected_user,
#     }
#
#     return render(request, 'admins/admin-users-update-delete.html', context)

class UserUpdateView(UpdateView):

    template_name = 'admins/admin-users-update-delete.html'
    model = User
    form_class = AdminUserUpdateForm
    success_url = reverse_lazy('admins:users')

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Админка: редактирование пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)


# Удаление пользователя
# @user_passes_test(lambda u: u.is_staff)
# def user_delete(request, id):
#     user = User.objects.get(id=id)
#     user.is_active = False
#     user.save()
#     return HttpResponseRedirect(reverse('admins:users'))

# Объединим классы удаления и восстановления в общий класс, который просто меняет занчение is_active на противоположное
class UserDeleteRestoreView(DeleteView):

    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = not self.object.is_active
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDeleteRestoreView, self).dispatch(request, *args, **kwargs)


# Отображение списка категорий
# @user_passes_test(lambda u: u.is_staff)
# def categories(request):
#     context = {
#         'title': 'GeekShop - Админка: категории',
#         'categories': ProductCategory.objects.all()
#     }
#     return render(request, 'admins/admin-categories-read.html', context)


class CategoriesListView(ListView):

    model = ProductCategory
    template_name = 'admins/admin-categories-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoriesListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Админка: категории'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoriesListView, self).dispatch(request, *args, **kwargs)


# Добавление категории
# @user_passes_test(lambda u: u.is_staff)
# def category_add(request):
#     if request.method == 'POST':
#         form = AdminCategoryCreate(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:categories'))
#         else:
#             print(form.errors)
#     else:
#         form = AdminCategoryCreate()
#     context = {
#         'title': 'GeekShop - Админка: добавление категории',
#         'form': form,
#     }
#     return render(request, 'admins/admin-category-create.html', context)

class CategoryCreateView(CreateView):

    model = ProductCategory
    template_name = 'admins/admin-category-create.html'
    form_class = AdminCategoryCreate
    success_url = reverse_lazy('admins:categories')

    def get_context_data(self, **kwargs):
        context = super(CategoryCreateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Админка: добавление категории'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryCreateView, self).dispatch(request, *args, **kwargs)


# Редактирование категории
# @user_passes_test(lambda u: u.is_staff)
# def category_edit(request, id):
#     selected_category = ProductCategory.objects.get(id=id)
#     if request.method == 'POST':
#         form = AdminCategoryCreate(instance=selected_category, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:categories'))
#         else:
#             print(form.errors)
#     else:
#         form = AdminCategoryCreate(instance=selected_category, )
#     context = {
#         'title': 'GeekShop - Админка: Редактирование категории',
#         'form': form,
#         'selected_category': selected_category,
#     }
#     return render(request, 'admins/admin-category-edit.html', context)

class CategoryUpdateView(UpdateView):

    model = ProductCategory
    template_name = 'admins/admin-category-edit.html'
    form_class = AdminCategoryCreate
    success_url = reverse_lazy('admins:categories')

    def get_context_data(self, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Админка: Редактирование категории'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryUpdateView, self).dispatch(request, *args, **kwargs)


# Удаление категории
# @user_passes_test(lambda u: u.is_staff)
# def category_delete(request, id):
#     selected_category = ProductCategory.objects.get(id=id)
#     selected_category.delete()
#     return HttpResponseRedirect(reverse('admins:categories'))

class CategoryDeleteView(DeleteView):

    model = ProductCategory
    template_name = 'admins/admin-category-edit.html'
    success_url = reverse_lazy('admins:categories')

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryDeleteView, self).dispatch(request, *args, **kwargs)


# Отображение списка продуктов
@user_passes_test(lambda u: u.is_staff)
def products(request):
    context = {
        'title': 'GeekShop - Админка: продукты',
        'products': Product.objects.all(),
    }
    return render(request, 'admins/admin-products-read.html', context)


# Добавление нового продукта
@user_passes_test(lambda u: u.is_staff)
def product_add(request):
    if request.method == 'POST':
        form = AdminProductCreateUpdate(files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:products'))
        else:
            print(form.errors)
    else:
        form = AdminProductCreateUpdate()
    context = {
        'title': 'GeekShop - Админка: добавление продукта',
        'form': form,
    }
    return render(request, 'admins/admin-product-create.html', context)


# Редактирование продукта
@user_passes_test(lambda u: u.is_staff)
def product_edit(request, id):
    selected_product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = AdminProductCreateUpdate(instance=selected_product, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:products'))
        else:
            print(form.errors)
    else:
        form = AdminProductCreateUpdate(instance=selected_product, )
    context = {
        'title': 'GeekShop - Админка: редактирование продукта',
        'form': form,
        'selected_product': selected_product
    }
    return render(request, 'admins/admin-product-edit.html', context)


@user_passes_test(lambda u: u.is_staff)
def product_delete(request, id):
    selected_product = Product.objects.get(id=id)
    selected_product.delete()
    return HttpResponseRedirect(reverse('admins:products'))