from rest_framework import serializers
from .models import CampaignArea


class CampaignAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignArea
        fields = [
            "id", "district_name", "slug", "province", "geographic_region",
            "description", "estimated_population", "healthcare_situation",
            "internet_mobile_situation", "major_health_challenges",
            "digital_health_needs", "campaign_activities_summary",
            "featured_image", "status", "map_x", "map_y",
        ]
