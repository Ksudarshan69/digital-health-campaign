from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "subject", "email", "submitted_at", "is_read")
    list_filter = ("is_read",)
    search_fields = ("name", "email", "subject", "message")
    list_editable = ("is_read",)
    date_hierarchy = "submitted_at"
