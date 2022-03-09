# Third Party
from django import forms
from tinymce.widgets import TinyMCE

from .models import NewsModel


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class NewsForm(forms.ModelForm):
    class Meta:
        model = NewsModel
        fields = ["title", "news"]
        labels = {"titel": "Überschrift", "news": "Deine Nachricht"}
        title = forms.CharField(max_length=50)
        news = forms.CharField(
            widget=TinyMCEWidget(attrs={"required": False, "cols": 30, "rows": 10})
        )

    class Media:
        js = (
            "/static/js/tinymce/news_form/news_form_textareas.js",
            "",
        )
