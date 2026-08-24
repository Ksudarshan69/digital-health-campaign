from rest_framework import viewsets
from .models import CampaignArea
from .serializers import CampaignAreaSerializer


class CampaignAreaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CampaignArea.objects.all()
    serializer_class = CampaignAreaSerializer
    filterset_fields = ["province", "status"]
    search_fields = ["district_name", "description"]
    lookup_field = "slug"
