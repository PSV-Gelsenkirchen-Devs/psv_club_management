# Third Party
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Team


@login_required
def index(request):
    """

    Args:
        request:

    Returns:
        HttpResponse: Returns the Content Page with a User List
    """
    return render(request, "teams/content.html")


@login_required
def teams_list(request):
    teams = Team.objects.order_by("name")
    return render(request, "teams/teams_list.html", {"teams": teams})
