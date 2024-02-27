from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'first_name', 'last_name', 'age', 'phone_number', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'password_save')}),  # Include 'password_save' field
        ('Personal Info', {'fields': ('first_name', 'last_name', 'age', 'phone_number', 'image')}),  # Include 'image' field
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'password_save', 'image'),  # Include 'image' field
        }),
    )
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
