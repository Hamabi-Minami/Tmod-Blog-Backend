from django.contrib import admin
from apps.UserManager.models.user import UserModel


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'gender',
        'account',
        'password',
        'email'
    )



