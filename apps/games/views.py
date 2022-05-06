# Third Party
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .models import Game


@login_required
def index(request):
    """

    Args:
        request:

    Returns:
        HttpResponse: Returns the Content Page with a User List
    """
    return render(request, "games/content.html")


@login_required
def games_list(request):
    games = Game.objects.order_by("game_day")
    return render(request, "games/games_list.html", {"games": games})


@login_required
def detail_view(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    return render(request, "games/detail.html", {"game": game})
