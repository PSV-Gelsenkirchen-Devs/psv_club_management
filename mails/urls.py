from django.urls import path

from . import views

app_name = "mails"
urlpatterns = [
    path("send/", views.send_mail_view, name="mail"),
]
