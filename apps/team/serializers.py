from rest_framework import serializers
from .models import TeamMember, TeamCategory


class TeamCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamCategory
        fields = ["id", "name"]


class TeamMemberSerializer(serializers.ModelSerializer):
    category = TeamCategorySerializer(read_only=True)

    class Meta:
        model = TeamMember
        fields = ["id", "full_name", "slug", "photo", "position", "category",
                  "district_location", "education", "experience", "skills",
                  "responsibilities", "biography", "facebook_url", "linkedin_url", "twitter_url"]
