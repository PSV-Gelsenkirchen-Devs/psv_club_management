# Third Party
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Account


class AccountAdmin(UserAdmin):
    list_display = (
        "email",
        "first_name",
        "last_name",
        "birthdate",
        "gender",
        "last_login",
        "date_joined",
        "is_member",
        "is_board",
        "is_coach",
        "is_staff",
        "is_superuser",
    )
    search_fields = (
        "email",
        "first_name",
        "last_name",
        "birthdate" "is_admin",
        "is_member",
        "is_board",
        "is_coach",
        "is_active",
    )
    readonly_fields = ("date_joined", "last_login")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "birthdate",
                    "gender",
                ),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_admin",
                    "is_member",
                    "is_board",
                    "is_coach",
                    "is_active",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "birthdate",
                    "gender",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )


admin.site.register(Account, AccountAdmin)
