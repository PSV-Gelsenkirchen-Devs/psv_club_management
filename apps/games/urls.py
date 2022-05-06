# Third Party
from django.urls import path

from . import views


app_name = "games"
urlpatterns = [
    path("", views.index, name="index"),
    path("games_list/", views.games_list, name="games_list"),
    path("<int:game_id>/", views.detail_view, name="detail_view"),
]
