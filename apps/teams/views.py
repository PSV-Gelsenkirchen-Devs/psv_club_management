# Third Party
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

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
def teams_view(request):
    return render(request, "teams/teams_index.html", {"teams": teams})
