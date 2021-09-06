from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
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
class CategoryDeleteView(DeleteView):

    model = ProductCategory
    template_name = 'admins/admin-category-edit.html'
    success_url = reverse_lazy('admins:categories')

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryDeleteView, self).dispatch(request, *args, **kwargs)


# Отображение списка продуктов
class ProductsListView(ListView):

    model = Product
    template_name = 'admins/admin-products-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Админка: продукты'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductsListView, self).dispatch(request, *args, **kwargs)


# Добавление нового продукта
class ProductCreateView(CreateView):

    model = Product
    template_name = 'admins/admin-product-create.html'
    form_class = AdminProductCreateUpdate
    success_url = reverse_lazy('admins:products')

    def get_context_data(self, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Админка: добавление продукта'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCreateView, self).dispatch(request, *args, **kwargs)


# Редактирование продукта
class ProductUpdateView(UpdateView):

    model = Product
    template_name = 'admins/admin-product-edit.html'
    form_class = AdminProductCreateUpdate
    success_url = reverse_lazy('admins:products')

    def get_context_data(self, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Админка: редактирование продукта'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductUpdateView, self).dispatch(request, *args, **kwargs)


# Удаление продукта
class ProductDeleteView(DeleteView):

    model = Product
    template_name = 'admins/admin-product-edit.html'
    success_url = reverse_lazy('admins:products')

    @method_decorator(user_passes_test(lambda u:u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductDeleteView, self).dispatch(request, *args, **kwargs)
