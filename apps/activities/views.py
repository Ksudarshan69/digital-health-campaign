from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Activity


def activity_list(request):
    activities = Activity.objects.filter(is_published=True)
    paginator = Paginator(activities, 9)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(request, "activities/list.html", {"page_obj": page_obj})


def activity_detail(request, slug):
    activity = get_object_or_404(Activity, slug=slug, is_published=True)
    return render(request, "activities/detail.html", {"activity": activity})
