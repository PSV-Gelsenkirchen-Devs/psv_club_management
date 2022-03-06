# Third Party
from django.urls import path

from . import views


app_name = "account"
urlpatterns = [
    path("", views.index, name="index"),
    path("/user_list", views.user_list_view, name="user_list_view"),
    path("<int:user_id>", views.profil_view, name="profil_view"),
]
