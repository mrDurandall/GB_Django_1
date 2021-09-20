from django.contrib import admin

from user.models import User, UserProfile
from basket.admin import BasketAdmin


admin.site.register(UserProfile)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (BasketAdmin, )

