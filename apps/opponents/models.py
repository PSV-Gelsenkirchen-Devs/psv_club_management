# Third Party
from django.db import models


class OppClub(models.Model):
    name = models.CharField(verbose_name="Verein", max_length=30)

    def __str__(self):
        return self.name


class OppPlayer(models.Model):
    club = models.ForeignKey(
        OppClub, verbose_name="Verein", on_delete=models.DO_NOTHING
    )
    first_name = models.CharField(verbose_name="Vorname", max_length=30)
    last_name = models.CharField(verbose_name="Nachname", max_length=30)

    def __str__(self):
        full_name = self.first_name + self.last_name
        return full_name


class OppTeam(models.Model):
    name = models.CharField(verbose_name="OppTeamName", max_length=15)
    club = models.ForeignKey(OppClub, on_delete=models.CASCADE)
    player = models.ManyToManyField(OppPlayer, blank=True)

    def __str__(self):
        full_name = self.club.name + " - " + self.name
        return full_name
