# Third Party
from django.urls import path

from . import views


app_name = "account"
urlpatterns = [
    path("", views.index, name="index"),
<<<<<<< HEAD:apps/account/urls.py
    path("user_list", views.user_list_view, name="user_list_view"),
=======
    path("/user_list", views.user_list_view, name="user_list_view"),
>>>>>>> ea137c7 (add Bootstrap to scss, show User Profil as Modal with Bootstrap and htmx):account/urls.py
    path("<int:user_id>", views.profil_view, name="profil_view"),
]
