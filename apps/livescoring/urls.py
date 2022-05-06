# Third Party
from django.urls import path

from . import views


app_name = "livescoring"

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "active_livescoring/",
        views.active_livescoring,
        name="active_livescoring",
    ),
    path("matches/", views.todays_matches, name="matches"),
]
