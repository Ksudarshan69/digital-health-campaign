from django.contrib import admin
from .models import HealthTool, PreventiveHealthTopic


@admin.register(HealthTool)
class HealthToolAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "is_published", "updated_at")
    list_filter = ("category", "is_published")
    search_fields = ("name", "short_description")
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ("is_published",)


@admin.register(PreventiveHealthTopic)
class PreventiveHealthTopicAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_published", "updated_at")
    list_filter = ("category", "is_published")
    search_fields = ("title", "summary")
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ("is_published",)
