from django.urls import path
from . import views

app_name = "health"

urlpatterns = [
    path("tools/", views.tool_list, name="tools"),
    path("tools/<slug:slug>/", views.tool_detail, name="tool_detail"),
    path("preventive/", views.preventive_list, name="preventive"),
    path("preventive/<slug:slug>/", views.preventive_detail, name="preventive_detail"),
]
