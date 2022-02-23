from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST

from .forms import LoginForm, OddNumberForm


def index(request):
    return render(request, "web/_base.html")


def login_view(request):
    if request.user.is_authenticated:
        return redirect(reverse("web:index"))
    login_form = LoginForm(request.POST or None)
    if request.POST and login_form.is_valid():
        user = login_form.login(request)
        if user:
            login(request, user)
            return redirect(reverse("news:index"))
    return render(request, "web/login.html", {"login_form": login_form})

def logout_view(request):
    logout(request)
    return redirect(reverse("web:index"))


@require_POST
def csrf_demo_checker(request: HttpRequest) -> HttpResponse:
    form = OddNumberForm(request.POST)
    if form.is_valid():
        number = form.cleaned_data["number"]
        number_is_odd = number % 2 == 1
    else:
        number_is_odd = False
    return render(
        request,
        "web/demo.html",
        {"form": form, "number_is_odd": number_is_odd},
    )
