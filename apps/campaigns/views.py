from django.shortcuts import render, get_object_or_404
from .models import CampaignArea


def area_list(request):
    areas = CampaignArea.objects.all()
    province = request.GET.get("province")
    if province:
        areas = areas.filter(province=province)
    return render(request, "campaigns/list.html", {
        "areas": areas,
        "provinces": CampaignArea._meta.get_field("province").choices,
        "selected_province": province,
    })


def area_detail(request, slug):
    area = get_object_or_404(CampaignArea, slug=slug)
    return render(request, "campaigns/detail.html", {"area": area})
