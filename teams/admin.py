# Third Party
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Team


class TeamAdmin(ModelAdmin):
    list_display = (
        "name",
        "league",
        "team_capitan",
        "get_player",
        "league_link",
    )
    search_fields = ("team_capitan", "name", "player", "league", "league_link")
    readonly_fields = ()

    filter_horizontal = ("player",)
    list_filter = ()
    fieldsets = (
        (
            None,
            {
                "fields": ("name", "league", "team_capitan", "player", "league_link"),
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
                    "name",
                    "league",
                    "team_capitan",
                    "player",
                    "league_link",
                ),
            },
        ),
    )

    def get_player(self, obj):
        return ", ".join([str(p) for p in obj.player.all()])


admin.site.register(Team, TeamAdmin)
