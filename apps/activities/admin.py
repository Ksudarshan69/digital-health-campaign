from django.contrib import admin
from .models import Activity, ActivityImage


class ActivityImageInline(admin.TabularInline):
    model = ActivityImage
    extra = 1


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "location", "campaign_area", "participant_count", "is_published")
    list_filter = ("campaign_area", "is_published")
    search_fields = ("title", "description", "location")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "date"
    inlines = [ActivityImageInline]
    list_editable = ("is_published",)
