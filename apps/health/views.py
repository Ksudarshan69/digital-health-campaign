from django.shortcuts import render, get_object_or_404
from .models import HealthTool, PreventiveHealthTopic


def tool_list(request):
    tools = HealthTool.objects.filter(is_published=True)
    category = request.GET.get("category")
    if category:
        tools = tools.filter(category=category)
    return render(request, "health/tools.html", {
        "tools": tools,
        "categories": HealthTool._meta.get_field("category").choices,
        "selected_category": category,
    })


def tool_detail(request, slug):
    tool = get_object_or_404(HealthTool, slug=slug, is_published=True)
    return render(request, "health/tool_detail.html", {"tool": tool})


def preventive_list(request):
    topics = PreventiveHealthTopic.objects.filter(is_published=True)
    category = request.GET.get("category")
    if category:
        topics = topics.filter(category=category)
    return render(request, "health/preventive.html", {
        "topics": topics,
        "categories": PreventiveHealthTopic._meta.get_field("category").choices,
        "selected_category": category,
    })


def preventive_detail(request, slug):
    topic = get_object_or_404(PreventiveHealthTopic, slug=slug, is_published=True)
    return render(request, "health/preventive_detail.html", {"topic": topic})
