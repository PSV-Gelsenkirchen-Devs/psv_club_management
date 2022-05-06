# Third Party
from account.models import Account
from django.db import models
from django.forms import ValidationError
from django.urls import reverse
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
    start_time = models.DateTimeField(
        verbose_name="Startzeit", default=timezone.now
    )
    end_time = models.DateTimeField(
        verbose_name="Endzeit", default=timezone.now
    )
    created_at = models.DateTimeField(default=timezone.now)
    home = models.BooleanField(verbose_name="Heimspiel", default=True)

    def get_absolute_url(self):
        return reverse("games:detail_view", kwargs={"game.id": self.pk})

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError("Ending times must after starting times")
