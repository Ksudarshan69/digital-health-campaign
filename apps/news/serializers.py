from rest_framework import serializers
from .models import NewsPost


class NewsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPost
        fields = ["id", "title", "slug", "category", "featured_image", "summary",
                  "content", "author", "published_date"]
