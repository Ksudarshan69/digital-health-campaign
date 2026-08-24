from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("mission/", views.mission, name="mission"),
    path("objectives/", views.objectives, name="objectives"),
]
