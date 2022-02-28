# Third Party
from django.db import models


class OppClub(models.Model):
    name = models.CharField(verbose_name="OppClubName", max_length=30)


class OppPlayer(models.Model):
    club = models.ForeignKey(OppClub, on_delete=models.DO_NOTHING)
    first_name = models.CharField(verbose_name="FirstName", max_length=30)
    last_name = models.CharField(verbose_name="LastName", max_length=30)


class OppTeam(models.Model):
    name = models.CharField(verbose_name="OppTeamName", max_length=15)
    club = models.ForeignKey(OppClub, on_delete=models.CASCADE)
    player = models.ManyToManyField(OppPlayer)
