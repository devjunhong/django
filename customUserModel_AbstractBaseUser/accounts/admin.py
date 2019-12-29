from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User


class AddUserForm(forms.ModelForm):
    """
    New User Form. Requires password confirmation.
    """

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


class UpdateUserForm(forms.ModelForm):
    """
    Update User Form. Doesn't allow changing password in the Admin.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = (
            'email', 'password', 'first_name', 'last_name', 'is_active',
            'is_staff'
        )

    def clean_password(self):
        # Password can't be changed in the admin
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    form = UpdateUserForm
    add_form = AddUserForm

    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', )
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email', 'username', 'first_name', 'last_name', 'password'
                )
            }
        ),
    )
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('email', 'username', 'first_name', 'last_name')
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
