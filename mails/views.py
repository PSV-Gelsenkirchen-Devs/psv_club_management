from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render


@login_required
def send_mail_view(request):
    send_mail(
        "Subject here" + request.user.first_name,
        "Here is the message.",
        "webmaster@badminton.psv-gelsenkirchen.de",
        ["sven.hoyer@hotmail.com"],
        fail_silently=False,
    )
    return render(request, "mails/content.html")
