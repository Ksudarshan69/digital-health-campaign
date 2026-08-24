from rest_framework import serializers
from .models import GalleryAlbum, GalleryMedia


class GalleryMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryMedia
        fields = ["id", "media_type", "image", "video_url", "caption"]


class GalleryAlbumSerializer(serializers.ModelSerializer):
    media_items = GalleryMediaSerializer(many=True, read_only=True)

    class Meta:
        model = GalleryAlbum
        fields = ["id", "title", "slug", "category", "cover_image", "description", "media_items"]
