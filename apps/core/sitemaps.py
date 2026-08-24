from django.contrib.sitemaps import Sitemap
from apps.campaigns.models import CampaignArea
from apps.health.models import HealthTool, PreventiveHealthTopic
from apps.resources.models import Resource
from apps.activities.models import Activity
from apps.news.models import NewsPost
from apps.team.models import TeamMember


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = "monthly"

    def items(self):
        return ["core:home", "core:about", "core:mission", "core:objectives"]

    def location(self, item):
        from django.urls import reverse
        return reverse(item)


class CampaignAreaSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return CampaignArea.objects.all()


class HealthToolSitemap(Sitemap):
    changefreq = "monthly"

    def items(self):
        return HealthTool.objects.filter(is_published=True)


class PreventiveHealthTopicSitemap(Sitemap):
    changefreq = "monthly"

    def items(self):
        return PreventiveHealthTopic.objects.filter(is_published=True)


class ResourceSitemap(Sitemap):
    changefreq = "monthly"

    def items(self):
        return Resource.objects.filter(is_published=True)


class ActivitySitemap(Sitemap):
    changefreq = "weekly"

    def items(self):
        return Activity.objects.filter(is_published=True)


class NewsPostSitemap(Sitemap):
    changefreq = "weekly"

    def items(self):
        return NewsPost.objects.filter(is_published=True)


class TeamMemberSitemap(Sitemap):
    changefreq = "yearly"

    def items(self):
        return TeamMember.objects.filter(is_active=True)


sitemaps = {
    "static": StaticViewSitemap,
    "campaign_areas": CampaignAreaSitemap,
    "health_tools": HealthToolSitemap,
    "preventive_health": PreventiveHealthTopicSitemap,
    "resources": ResourceSitemap,
    "activities": ActivitySitemap,
    "news": NewsPostSitemap,
    "team": TeamMemberSitemap,
}
