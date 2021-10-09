from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from admins.forms import AdminUserCreationFrom,\
                        AdminUserUpdateForm, \
                        AdminCategoryCreate, \
                        AdminProductCreateUpdate
from user.models import User
from products.models import ProductCategory, Product
from common.views import CommonContextMixin, IsStaffTestMixin


# Главная админки
class AdminIndexView(IsStaffTestMixin, CommonContextMixin, TemplateView):

    template_name = 'admins/index.html'
    title = 'GeekShop - Админка: Главная'


# Список пользователей
class UsersListView(IsStaffTestMixin, CommonContextMixin, ListView):

    template_name = 'admins/admin-users-read.html'
    model = User
    title = 'GeekShop - Админка: пользователи'


# Добавление пользователей
class UserCreateView(IsStaffTestMixin, CommonContextMixin, CreateView):

    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = AdminUserCreationFrom
    success_url = reverse_lazy('admins:users')
    title = 'GeekShop - Админка: создание пользователя'


# Изменение пользователя
class UserUpdateView(IsStaffTestMixin, CommonContextMixin, UpdateView):

    template_name = 'admins/admin-users-update-delete.html'
    model = User
    form_class = AdminUserUpdateForm
    success_url = reverse_lazy('admins:users')
    title = 'GeekShop - Админка: редактирование пользователя'


# Удаление пользователя
# Объединим классы удаления и восстановления в общий класс, который просто меняет занчение is_active на противоположное
class UserDeleteRestoreView(IsStaffTestMixin, DeleteView):

    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = not self.object.is_active
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# Отображение списка категорий
class CategoriesListView(IsStaffTestMixin, CommonContextMixin, ListView):

    model = ProductCategory
    template_name = 'admins/admin-categories-read.html'
    title = 'GeekShop - Админка: категории'


# Добавление категории
# @user_passes_test(lambda u: u.is_staff)
class CategoryCreateView(IsStaffTestMixin, CommonContextMixin, CreateView):

    model = ProductCategory
    template_name = 'admins/admin-category-create.html'
    form_class = AdminCategoryCreate
    success_url = reverse_lazy('admins:categories')
    title = 'GeekShop - Админка: добавление категории'


# Редактирование категории
class CategoryUpdateView(IsStaffTestMixin, CommonContextMixin, UpdateView):

    model = ProductCategory
    template_name = 'admins/admin-category-edit.html'
    form_class = AdminCategoryCreate
    success_url = reverse_lazy('admins:categories')
    title = 'GeekShop - Админка: Редактирование категории'


# Удаление категории
class CategoryDeleteView(IsStaffTestMixin, DeleteView):

    model = ProductCategory
    template_name = 'admins/admin-category-edit.html'
    success_url = reverse_lazy('admins:categories')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = not self.object.is_active
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# Отображение списка продуктов
class ProductsListView(IsStaffTestMixin, CommonContextMixin, ListView):

    model = Product
    template_name = 'admins/admin-products-read.html'
    title = 'GeekShop - Админка: продукты'


# Добавление нового продукта
class ProductCreateView(IsStaffTestMixin, CommonContextMixin, CreateView):

    model = Product
    template_name = 'admins/admin-product-create.html'
    form_class = AdminProductCreateUpdate
    success_url = reverse_lazy('admins:products')
    title = 'GeekShop - Админка: добавление продукта'


# Редактирование продукта
class ProductUpdateView(IsStaffTestMixin, CommonContextMixin, UpdateView):

    model = Product
    template_name = 'admins/admin-product-edit.html'
    form_class = AdminProductCreateUpdate
    success_url = reverse_lazy('admins:products')
    title = 'GeekShop - Админка: редактирование продукта'


# Удаление продукта
class ProductDeleteView(IsStaffTestMixin, DeleteView):

    model = Product
    template_name = 'admins/admin-product-edit.html'
    success_url = reverse_lazy('admins:products')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = not self.object.is_active
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
