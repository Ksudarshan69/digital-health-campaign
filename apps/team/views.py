from django.shortcuts import render, get_object_or_404
from .models import TeamMember, TeamCategory


def team_list(request):
    members = TeamMember.objects.filter(is_active=True)
    category = request.GET.get("category")
    if category:
        members = members.filter(category__id=category)
    return render(request, "team/list.html", {
        "members": members,
        "categories": TeamCategory.objects.all(),
        "selected_category": category,
    })


def team_detail(request, slug):
    member = get_object_or_404(TeamMember, slug=slug, is_active=True)
    return render(request, "team/detail.html", {"member": member})
