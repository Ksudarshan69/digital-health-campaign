from django.shortcuts import render
from apps.campaigns.models import CampaignArea
from apps.health.models import HealthTool, PreventiveHealthTopic
from apps.activities.models import Activity
from apps.resources.models import Resource
from apps.news.models import NewsPost


def home(request):
    context = {
        "campaign_areas": CampaignArea.objects.all()[:6],
        "health_tools": HealthTool.objects.filter(is_published=True)[:4],
        "preventive_topics": PreventiveHealthTopic.objects.filter(is_published=True)[:3],
        "activities": Activity.objects.filter(is_published=True)[:3],
        "resources": Resource.objects.filter(is_published=True)[:3],
        "news_posts": NewsPost.objects.filter(is_published=True)[:3],
    }
    return render(request, "home/index.html", context)


def about(request):
    return render(request, "home/about.html")


def mission(request):
    return render(request, "home/mission.html")


def objectives(request):
    objectives_list = [
        ("01", "Digital Health Awareness", "Building public understanding of what digital health tools are and how they help."),
        ("02", "Rural Health Information", "Getting reliable health information to communities far from health facilities."),
        ("03", "Preventive Healthcare", "Promoting early awareness so health problems are caught before they become serious."),
        ("04", "Digital Health Tools", "Introducing devices like BP monitors, glucose monitors, and pulse oximeters."),
        ("05", "Telemedicine Awareness", "Helping communities understand and access remote healthcare consultations."),
        ("06", "Youth Engagement", "Involving students and young volunteers as digital health ambassadors."),
        ("07", "Digital Skills", "Building basic digital literacy needed to use health apps and services."),
        ("08", "Technology Access", "Connecting communities with the tools and connectivity they need."),
    ]
    return render(request, "home/objectives.html", {"objectives_list": objectives_list})
