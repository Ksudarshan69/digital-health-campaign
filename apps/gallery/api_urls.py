from rest_framework.routers import DefaultRouter
from .api_views import GalleryAlbumViewSet

router = DefaultRouter()
router.register("", GalleryAlbumViewSet, basename="gallery-album")
urlpatterns = router.urls
