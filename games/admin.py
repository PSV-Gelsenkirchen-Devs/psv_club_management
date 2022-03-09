# Third Party
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Game


class GameAdmin(ModelAdmin):
    list_display = (
        "datetime",
        "game_day",
        "team",
        "opp_team",
        "home",
        "game_admin",
        "game_link",
    )
    search_fields = (
        "datetime",
        "game_day",
        "team",
        "opp_team",
        "home",
        "game_admin",
        "game_link",
    )
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "datetime",
                    "game_day",
                    "team",
                    "opp_team",
                    "home",
                    "game_admin",
                    "game_link",
                ),
            },
        ),
        (
            "Permissions",
            {
                "fields": (),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "datetime",
                    "game_day",
                    "team",
                    "opp_team",
                    "home",
                    "game_admin",
                    "game_link",
                ),
            },
        ),
    )


admin.site.register(Game, GameAdmin)
