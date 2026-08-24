from django.contrib import admin
from .models import TeamCategory, TeamMember


@admin.register(TeamCategory)
class TeamCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "display_order")


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("full_name", "position", "category", "is_active", "display_order")
    list_filter = ("category", "is_active")
    search_fields = ("full_name", "position", "biography")
    prepopulated_fields = {"slug": ("full_name",)}
    list_editable = ("display_order", "is_active")
