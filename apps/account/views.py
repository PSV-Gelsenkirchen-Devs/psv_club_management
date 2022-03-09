"""Views from Account Package"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

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
