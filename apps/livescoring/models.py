# Third Party
from account.models import Account
from django.db import models
from django.urls import reverse
from django.utils import timezone
from games.models import Game
from opponents.models import OppPlayer


class Point(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class Set(models.Model):
    last_modified = models.DateTimeField(auto_now=True)
    set_number = models.IntegerField(default=1)
    points_team = models.ManyToManyField(
        Point, related_name="points_team", verbose_name="Punkte PSV"
    )
    points_opp_team = models.ManyToManyField(
        Point, related_name="points_opp_team", verbose_name="Punkte Gegner"
    )


class MatchGame(models.Model):
    last_modified = models.DateTimeField(auto_now=True)
    GAME_TYPE = [
        ("MD1", "1. Herrendoppel"),
        ("MD2", "2. Herrendoppel"),
        ("WD", "Damendoppel"),
        ("MS1", "1. Herreneinzel"),
        ("MS2", "2. Herreneinzel"),
        ("MS3", "3. Herreneinzel"),
        ("WS", "Dameneinzel"),
        ("XD", "Gemischtes Doppel"),
    ]
    game_type = models.CharField(
        verbose_name="Spiel",
        max_length=15,
        choices=GAME_TYPE,
    )

    Team = "T"
    OPPTeam = "O"
    WINNER = [
        (Team, "Team"),
        (OPPTeam, "Gegner"),
        (None, "Keiner"),
    ]

    player_team1 = models.ManyToManyField(Account, verbose_name="Spieler")
    player_oppTeam1 = models.ManyToManyField(
        OppPlayer, verbose_name="Spieler Gegner"
    )

    winner = models.CharField(
        verbose_name="Winner", max_length=10, choices=WINNER
    )

    sets = models.ManyToManyField(Set, verbose_name="Sätze", blank=True)
    current_set = models.IntegerField(default=0)


class Match(models.Model):
    last_modified = models.DateTimeField(auto_now=True)
    HOME = "H"
    AWAY = "A"
    DRAW = "D"
    WINNER = [
        (HOME, "Heim"),
        (AWAY, "Auswärts"),
        (DRAW, "Unentschieden"),
        (None, "Keiner"),
    ]
    game = models.ForeignKey(
        Game, verbose_name="Spiel", on_delete=models.CASCADE
    )
    games = models.ManyToManyField(MatchGame, verbose_name="Spiele")
    created_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(verbose_name="Spiel Aktiv", default=True)
    score_team = models.IntegerField(verbose_name="Punkte PSV", default=0)
    score_opponents = models.IntegerField(
        verbose_name="Punkte Gegner", default=0
    )

    winner = models.CharField(
        verbose_name="Gewonnen",
        max_length=5,
        choices=WINNER,
        default=None,
        null=True,
    )

    def get_absolute_url(self):
        return reverse("games:detail_view", kwargs={"game.id": self.pk})
