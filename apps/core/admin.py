from django.contrib import admin
from .models import CampaignSettings


@admin.register(CampaignSettings)
class CampaignSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Identity", {"fields": ("campaign_name", "slogan", "logo")}),
        ("Homepage content", {"fields": ("hero_title", "hero_description", "mission", "introduction")}),
        ("Statistics", {"fields": ("stat_districts", "stat_people_reached", "stat_programs", "stat_volunteers")}),
        ("Contact", {"fields": ("contact_address", "contact_phone", "contact_email")}),
        ("Social media", {"fields": ("facebook_url", "instagram_url", "linkedin_url", "youtube_url")}),
    )

    def has_add_permission(self, request):
        # Singleton: block adding a second row once one exists
        return not CampaignSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
