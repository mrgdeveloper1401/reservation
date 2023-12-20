from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User



@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("mobile_phone", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "create_at", "update_at")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("mobile_phone", "password1", "password2"),
            },
        ),
    )
    list_display = ("mobile_phone", "email", "first_name", "last_name", "is_staff", "is_active", 'is_superuser')
    search_fields = ("mobile_phone", "first_name", "last_name", "email")
    ordering = ('mobile_phone',)
    readonly_fields = ('create_at', 'update_at')
    list_filter = ('create_at', 'update_at', 'is_active', 'is_staff', 'is_superuser')

