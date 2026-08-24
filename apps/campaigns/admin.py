from django.contrib import admin
from .models import CampaignArea, CampaignAreaImage


class CampaignAreaImageInline(admin.TabularInline):
    model = CampaignAreaImage
    extra = 1


@admin.register(CampaignArea)
class CampaignAreaAdmin(admin.ModelAdmin):
    list_display = ("district_name", "province", "status", "estimated_population", "updated_at")
    list_filter = ("province", "status")
    search_fields = ("district_name", "description")
    prepopulated_fields = {"slug": ("district_name",)}
    inlines = [CampaignAreaImageInline]
    fieldsets = (
        (None, {"fields": ("district_name", "slug", "province", "geographic_region", "status", "featured_image")}),
        ("Content", {"fields": ("description", "healthcare_situation", "internet_mobile_situation",
                                 "major_health_challenges", "digital_health_needs", "campaign_activities_summary")}),
        ("Data", {"fields": ("estimated_population",)}),
        ("Map position", {"fields": ("map_x", "map_y"), "description": "Position (0-100) on the districts overview grid."}),
    )
