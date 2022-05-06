# Third Party
from django.urls import path

from . import views


app_name = "psv_calendar"

urlpatterns = [
    path("", views.index, name="index"),
    path("calendar/", views.CalendarView.as_view(), name="calendar"),  # here
]
