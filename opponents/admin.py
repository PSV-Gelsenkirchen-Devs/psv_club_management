# Third Party
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import OppClub, OppPlayer, OppTeam


class OppClubAdmin(ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (
            None,
            {"fields": ("name",)},
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
                "fields": ("name",),
            },
        ),
    )

    def get_player(self, obj):
        return ", ".join([str(p) for p in obj.player.all()])


class OppTeamAdmin(ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (
            None,
            {"fields": ("name",)},
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
                "fields": ("name",),
            },
        ),
    )

    def get_player(self, obj):
        return ", ".join([str(p) for p in obj.player.all()])


class OppPlayerAdmin(ModelAdmin):
    list_display = ("club", "first_name", "last_name")
    search_fields = ("club", "first_name", "last_name")
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (
            None,
            {"fields": ("club", "first_name", "last_name")},
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
                "fields": ("club", "first_name", "last_name"),
            },
        ),
    )


class OppTeamAdmin(ModelAdmin):
    list_display = ("name", "club", "get_player")
    search_fields = ("name", "club", "player")
    readonly_fields = ()

    filter_horizontal = ("player",)
    list_filter = ()
    fieldsets = (
        (
            None,
            {"fields": ("name", "club", "player")},
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
                "fields": ("name", "club", "player"),
            },
        ),
    )

    def get_player(self, obj):
        return ", ".join([str(p) for p in obj.player.all()])


admin.site.register(OppClub, OppClubAdmin)
admin.site.register(OppTeam, OppTeamAdmin)
admin.site.register(OppPlayer, OppPlayerAdmin)
