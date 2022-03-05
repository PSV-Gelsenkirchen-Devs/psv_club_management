<<<<<<< HEAD:apps/teams/views.py
=======
"""Views from Account Package"""
>>>>>>> 8811189 (add frist example of Profil page):account/views.py
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

<<<<<<< HEAD:apps/teams/views.py

@login_required
def teams_view(request):
    teams = Team.objects.order_by("name")
    return render(request, "teams/teams_index.html", {"teams": teams})
=======
    accounts = Account.objects.all()
    context["accounts"] = accounts
    return render(request, "account/content.html", context)


@login_required
def profil_view(request, user_id):
    user = get_object_or_404(Account, id=user_id)
    return render(request, "account/profil.html", {"user": user})
>>>>>>> 8811189 (add frist example of Profil page):account/views.py
