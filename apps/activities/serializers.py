from rest_framework import serializers
from .models import Activity


class ActivitySerializer(serializers.ModelSerializer):
    campaign_area_name = serializers.CharField(source="campaign_area.district_name", read_only=True)

    class Meta:
        model = Activity
        fields = ["id", "title", "slug", "date", "location", "campaign_area", "campaign_area_name",
                  "description", "participant_count", "featured_image", "content"]
