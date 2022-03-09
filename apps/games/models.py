# Standard Library
from operator import mod

# Third Party
from account.models import Account
from django.db import models
from django.utils import timezone
from opponents.models import OppTeam
from teams.models import Team


class Game(models.Model):

    game_admin = models.ForeignKey(
        Account, verbose_name="Spiel Admin", on_delete=models.DO_NOTHING
    )
    team = models.ForeignKey(
        Team,
        verbose_name="Mannschaft",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    opp_team = models.ForeignKey(
        OppTeam,
        verbose_name="Gegner",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    game_day = models.IntegerField(verbose_name="Spieltag", default=0)
    game_link = models.URLField(
        verbose_name="Turnier.de", blank=True, null=True
    )
    datetime = models.DateTimeField(verbose_name="datetime")
    created_at = models.DateTimeField(default=timezone.now)
    home = models.BooleanField(verbose_name="Heimspiel", default=True)
    winner = models.BooleanField(verbose_name="Gewonnen", default=None)
    points_team = models.IntegerField(verbose_name="Punkte PSV", default=0)
    points_opponents = models.IntegerField(
        verbose_name="Punkte Gegner", default=0
    )
