from django.urls import path

from . import views

app_name = "web"
urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("demo/", views.csrf_demo_checker, name="demo"),
]
