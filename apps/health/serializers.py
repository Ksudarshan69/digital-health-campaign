from rest_framework import serializers
from .models import HealthTool, PreventiveHealthTopic


class HealthToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthTool
        fields = ["id", "name", "slug", "icon_image", "short_description",
                  "detailed_content", "category", "created_at", "updated_at"]


class PreventiveHealthTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreventiveHealthTopic
        fields = ["id", "title", "slug", "category", "featured_image", "summary",
                  "detailed_content", "created_at", "updated_at"]
