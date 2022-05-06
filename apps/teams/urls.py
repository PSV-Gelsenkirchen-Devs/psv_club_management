# Third Party
from django.urls import path

from . import views


app_name = "teams"
urlpatterns = [
    path("", views.index, name="index"),
    path("teams_list/", views.teams_list, name="teams_list"),
]
