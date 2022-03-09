# Third Party
from django.urls import path

from . import views


app_name = "teams"
urlpatterns = [
    path("", views.index, name="index"),
    path("teams_index/", views.teams_view, name="teams_view"),
]
