from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Account


class AccountAdmin(UserAdmin):
    list_display = (
        "last_name",
        "first_name",
        "email",
        "last_login",
        "date_joined",
        "is_admin",
        "is_staff",
    )
    search_fields = ("first_name", "last_name", "email", "is_admin", "is_staff")
    readonly_fields = ("date_joined", "last_login")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (
            None,
            {
                "fields": ("first_name", "last_name", "email", "birthdate"),
            },
        ),
        (
            "Permissions",
            {
                "fields": ("is_staff", "is_active"),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "birthdate",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )


admin.site.register(Account, AccountAdmin)
