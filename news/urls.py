# Third Party
from django.urls import include, path

from . import views


app_name = "news"
urlpatterns = [
    path("", views.index, name="index"),
    path("news_index/", views.index_view, name="index_view"),
    path("news_form/", views.news_form_view, name="form_view"),
    path("news_timeline/", views.timeline_view, name="timeline_view"),
    path("create-news/", views.create_news_view, name="create_news"),
    path("<int:post_id>/delete/", views.delete_news_view, name="delete_news"),
    path("tinymce/", include("tinymce.urls")),
]
