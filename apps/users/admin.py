from django.contrib import admin

from apps.users.models import User, Confirmation


@admin.register(Confirmation)
class ConfirmationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'phone', 'code', 'time_limit', 'is_confirmed')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'phone', 'auth_status')
