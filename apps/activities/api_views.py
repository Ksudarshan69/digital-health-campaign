from rest_framework import viewsets
from .models import Activity
from .serializers import ActivitySerializer


class ActivityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Activity.objects.filter(is_published=True)
    serializer_class = ActivitySerializer
    filterset_fields = ["campaign_area"]
    search_fields = ["title", "description", "location"]
    lookup_field = "slug"
