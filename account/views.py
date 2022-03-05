"""Views from Account Package"""
# Third Party
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .models import Account


@login_required
def index(request):
    """

    Args:
        request:

    Returns:
        HttpResponse: Returns the Content Page with a User List
    """
    context = {}

    accounts = Account.objects.all()
    context["accounts"] = accounts
    return render(request, "account/content.html", context)


@login_required
def profil_view(request, user_id):
    user = get_object_or_404(Account, id=user_id)
    return render(request, "account/profil.html", {"user": user})
