# Standard Library
from datetime import datetime

# Third Party
from django.shortcuts import render
from games.models import Game

from .models import Match


def index(request):
    return render(request, "livescoring/content.html")


def active_livescoring(request):
    games = Match.objects.filter(active=True).order_by("game__start_time")
    return render(
        request, "livescoring/active_livescoring_list.html", {"games": games}
    )


def todays_matches(request):
    today = datetime.today().date()
    games = Game.objects.filter(start_time__date=today).order_by("start_time")
    return render(request, "livescoring/match_list.html", {"games": games})
