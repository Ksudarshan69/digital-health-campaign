from rest_framework import viewsets
from .models import HealthTool, PreventiveHealthTopic
from .serializers import HealthToolSerializer, PreventiveHealthTopicSerializer


class HealthToolViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HealthTool.objects.filter(is_published=True)
    serializer_class = HealthToolSerializer
    filterset_fields = ["category"]
    search_fields = ["name", "short_description"]
    lookup_field = "slug"


class PreventiveHealthTopicViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PreventiveHealthTopic.objects.filter(is_published=True)
    serializer_class = PreventiveHealthTopicSerializer
    filterset_fields = ["category"]
    search_fields = ["title", "summary"]
    lookup_field = "slug"
