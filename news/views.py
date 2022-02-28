# Third Party
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.decorators.http import require_POST

from .forms import NewsForm
from .models import NewsModel


def index(request):
    """

    Args:
        request:
        username:

    Returns:
        HttpResponse: Returns the News Timeline
    """
    return render(request, "news/content.html")


def index_view(request):
    """

    Args:
        request:
        username:

    Returns:
        HttpResponse: Returns the News Timeline
    """
    response = render(request, "news/news_index.html")
    response["HX-Trigger"] = "created_news"
    return response


def timeline_view(request):
    posts = NewsModel.objects.order_by("-created_at")
    return render(
        request,
        "news/timeline.html",
        {"posts": posts},
    )


@login_required
def news_form_view(request):
    news_form = NewsForm()
    context = {"news_form": news_form}
    return render(request, "news/news_form.html", context)


@login_required
@require_POST
def create_news_view(request):
    """View for the news create Form

    Args:
        request ([type]): [description]

    Returns:
        [HttpResponseRedirect]: Redirect to the news main page
    """
    news_form = NewsForm(request.POST)
    if news_form.is_valid():
        post = news_form.save(commit=False)
        post.user = request.user
        post.save()
    headers = {
        "HX-Trigger": "createdNews",
    }
    return HttpResponseRedirect(reverse("news:index_view"), headers=headers)


@login_required
def delete_news_view(request, post_id):
    post = get_object_or_404(NewsModel, id=post_id, user=request.user)
    post.delete()
    return HttpResponseRedirect(reverse("news:timeline_view"))
