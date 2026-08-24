from django.contrib import admin
from .models import Resource, ResourceCategory


@admin.register(ResourceCategory)
class ResourceCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "resource_type", "published_date", "is_published")
    list_filter = ("category", "resource_type", "is_published")
    search_fields = ("title", "description", "content")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "published_date"
    list_editable = ("is_published",)
