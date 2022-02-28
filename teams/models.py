# Third Party
from django.db import models

# Library
from account.models import Account


class TeamModel(models.Model):
    team_capitan = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    name = models.CharField(verbose_name="Team Name", max_length=15)
    player = models.ManyToManyField(Account)
