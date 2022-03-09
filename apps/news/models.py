# Third Party
from django.db import models
from django.utils import timezone
from tinymce import models as tinymce_models

# Library
from account.models import Account


class NewsModel(models.Model):
    """This Class saves the News

    Args:
        models ([type]): News save Model
    """

    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="title", max_length=50)
    news = tinymce_models.HTMLField()
    created_at = models.DateTimeField(default=timezone.now)
