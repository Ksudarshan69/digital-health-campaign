import csv
from django.contrib import admin
from django.http import HttpResponse
from .models import VolunteerApplication


@admin.action(description="Export selected applications as CSV")
def export_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = "attachment; filename=volunteer_applications.csv"
    writer = csv.writer(response)
    writer.writerow(["Full Name", "Age", "Gender", "District", "Education", "Phone",
                      "Email", "Skills", "Status", "Submitted At"])
    for app in queryset:
        writer.writerow([app.full_name, app.age, app.get_gender_display(), app.district,
                          app.education, app.phone_number, app.email, app.skills,
                          app.get_status_display(), app.submitted_at])
    return response


@admin.register(VolunteerApplication)
class VolunteerApplicationAdmin(admin.ModelAdmin):
    # Personal info stays admin-only per spec section 23 ("do not expose
    # volunteer personal information publicly") — no public-facing view exists.
    list_display = ("full_name", "district", "status", "submitted_at")
    list_filter = ("status", "district", "gender")
    search_fields = ("full_name", "email", "phone_number", "district")
    list_editable = ("status",)
    date_hierarchy = "submitted_at"
    actions = [export_as_csv]
