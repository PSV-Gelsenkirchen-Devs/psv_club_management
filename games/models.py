# Standard Library
from operator import mod

# Third Party
from django.db import models
from django.utils import timezone

# Library
from account.models import Account
from teams.models import TeamModel


class GameModel(models.Model):

    game_admin = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    team = models.ForeignKey(TeamModel, on_delete=models.CASCADE)
    datetime = models.DateTimeField(verbose_name="datetime")
    created_at = models.DateTimeField(default=timezone.now)
    home = models.BooleanField(verbose_name="HomeAdvantage", default=True)
    winner = models.BooleanField(verbose_name="Winner", default=None)
    points_team = models.IntegerField()
    points_opponents = models.IntegerField()
