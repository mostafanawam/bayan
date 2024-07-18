from django.contrib import admin

from main.form import CustomUserCreationForm
from main.models import Category, Program, User
from django.contrib.auth.models import Group

admin.site.unregister(Group)


class UserAdmin(admin.ModelAdmin):
    fields = [
        "username",
        'email','password',
        # 'is_staff','is_superuser','is_enabled'
    ]
    list_display = (
        'id',
        "username",
        'email',
        'is_staff',
        'is_enabled',
        'is_superuser',
        'last_login',
    ) 
    list_filter = ('is_staff',)
admin.site.register(User, UserAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        "name",
        "name_ar",
        "index",
        'is_enabled',
    ) 
admin.site.register(Category, CategoryAdmin)



class ProgramAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'category',
        'name',
        'index',
        'is_enabled'
    )
admin.site.register(Program, ProgramAdmin)
