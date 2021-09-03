from django.contrib import admin

from user.models import User
from basket.admin import BasketAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (BasketAdmin, )

