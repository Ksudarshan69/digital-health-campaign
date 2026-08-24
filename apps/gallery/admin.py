from django.contrib import admin
from .models import GalleryAlbum, GalleryMedia


class GalleryMediaInline(admin.TabularInline):
    model = GalleryMedia
    extra = 1


@admin.register(GalleryAlbum)
class GalleryAlbumAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created_at")
    list_filter = ("category",)
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [GalleryMediaInline]
