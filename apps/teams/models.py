# Third Party
from django.db import models

# Library
from account.models import Account


class Team(models.Model):
    name = models.CharField(
        verbose_name="Team Name", max_length=15, blank=True, null=True
    )
    league = models.CharField(verbose_name="Liga", max_length=15)
    league_link = models.URLField(verbose_name="Turnier.de", max_length=200)
    team_capitan = models.ForeignKey(
        Account,
        verbose_name="Mannschaftsführer",
        on_delete=models.DO_NOTHING,
        related_name="team_capitan",
        blank=True,
        null=True,
    )
    player = models.ManyToManyField(
        Account, verbose_name="Spieler", related_name="players", blank=True
    )

    def __str__(self):
        return self.name
