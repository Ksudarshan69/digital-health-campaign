from rest_framework import serializers
from .models import Resource, ResourceCategory


class ResourceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceCategory
        fields = ["id", "name", "slug"]


class ResourceSerializer(serializers.ModelSerializer):
    category = ResourceCategorySerializer(read_only=True)

    class Meta:
        model = Resource
        fields = ["id", "title", "slug", "thumbnail", "category", "resource_type",
                  "description", "content", "file", "external_video_url",
                  "author", "published_date"]
