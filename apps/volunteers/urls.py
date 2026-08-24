from django.urls import path
from . import views

app_name = "volunteers"

urlpatterns = [
    path("", views.join, name="join"),
]
