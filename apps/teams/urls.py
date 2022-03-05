# Third Party
from django.urls import path

from . import views


<<<<<<< HEAD:apps/teams/urls.py
app_name = "teams"
urlpatterns = [
    path("", views.index, name="index"),
    path("teams_index/", views.teams_view, name="teams_view"),
=======
app_name = "account"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:user_id>", views.profil_view, name="profil_view"),
>>>>>>> 8811189 (add frist example of Profil page):account/urls.py
]
