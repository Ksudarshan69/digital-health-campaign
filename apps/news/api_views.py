from rest_framework import viewsets
from .models import NewsPost
from .serializers import NewsPostSerializer


class NewsPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NewsPost.objects.filter(is_published=True)
    serializer_class = NewsPostSerializer
    filterset_fields = ["category"]
    search_fields = ["title", "summary", "content"]
    lookup_field = "slug"
