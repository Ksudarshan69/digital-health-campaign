"""
Root URL configuration. Public site uses server-rendered Django templates;
/api/ exposes the same content as JSON for the future mobile app clients
(spec section 39).
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from apps.core.sitemaps import sitemaps
from apps.core.robots_view import robots_txt

urlpatterns = [
    path("admin/", admin.site.urls),

    # Public site
    path("", include("apps.core.urls")),
    path("campaign-areas/", include("apps.campaigns.urls")),
    path("digital-health/", include("apps.health.urls")),
    path("resources/", include("apps.resources.urls")),
    path("activities/", include("apps.activities.urls")),
    path("news/", include("apps.news.urls")),
    path("team/", include("apps.team.urls")),
    path("gallery/", include("apps.gallery.urls")),
    path("join-campaign/", include("apps.volunteers.urls")),
    path("contact/", include("apps.contact.urls")),
    path("search/", include("apps.core.search_urls")),

    # DRF API (spec section 27)
    path("api/campaign-areas/", include("apps.campaigns.api_urls")),
    path("api/health-tools/", include("apps.health.api_urls")),
    path("api/preventive-health/", include("apps.health.api_preventive_urls")),
    path("api/resources/", include("apps.resources.api_urls")),
    path("api/activities/", include("apps.activities.api_urls")),
    path("api/news/", include("apps.news.api_urls")),
    path("api/team/", include("apps.team.api_urls")),
    path("api/gallery/", include("apps.gallery.api_urls")),

    # SEO
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path("robots.txt", robots_txt, name="robots_txt"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
