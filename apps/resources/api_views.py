from rest_framework import viewsets
from .models import Resource
from .serializers import ResourceSerializer


class ResourceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Resource.objects.filter(is_published=True)
    serializer_class = ResourceSerializer
    filterset_fields = ["category", "resource_type"]
    search_fields = ["title", "description", "content"]
    lookup_field = "slug"
