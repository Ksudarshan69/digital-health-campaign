from django.db.models import Q
from django.shortcuts import render
from apps.news.models import NewsPost
from apps.resources.models import Resource
from apps.activities.models import Activity
from apps.health.models import PreventiveHealthTopic
from apps.campaigns.models import CampaignArea
from apps.team.models import TeamMember


def global_search(request):
    """
    Site-wide search across News, Resources, Activities, Health topics,
    Campaign areas, and Team (spec section 30). Simple icontains matching —
    fine at this content scale; swap for Postgres full-text search if the
    dataset grows significantly.
    """
    query = request.GET.get("q", "").strip()
    results = {"news": [], "resources": [], "activities": [], "health_topics": [], "campaign_areas": [], "team": []}

    if query:
        results["news"] = NewsPost.objects.filter(is_published=True).filter(
            Q(title__icontains=query) | Q(summary__icontains=query))[:5]
        results["resources"] = Resource.objects.filter(is_published=True).filter(
            Q(title__icontains=query) | Q(description__icontains=query))[:5]
        results["activities"] = Activity.objects.filter(is_published=True).filter(
            Q(title__icontains=query) | Q(description__icontains=query))[:5]
        results["health_topics"] = PreventiveHealthTopic.objects.filter(is_published=True).filter(
            Q(title__icontains=query) | Q(summary__icontains=query))[:5]
        results["campaign_areas"] = CampaignArea.objects.filter(
            Q(district_name__icontains=query) | Q(description__icontains=query))[:5]
        results["team"] = TeamMember.objects.filter(is_active=True).filter(
            Q(full_name__icontains=query) | Q(position__icontains=query))[:5]

    total = sum(len(v) for v in results.values())
    return render(request, "search/results.html", {"query": query, "results": results, "total": total})
