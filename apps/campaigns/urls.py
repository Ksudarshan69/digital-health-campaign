from django.urls import path
from . import views

app_name = "campaigns"

urlpatterns = [
    path("", views.area_list, name="list"),
    path("<slug:slug>/", views.area_detail, name="detail"),
]
