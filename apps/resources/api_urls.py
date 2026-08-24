from rest_framework.routers import DefaultRouter
from .api_views import ResourceViewSet

router = DefaultRouter()
router.register("", ResourceViewSet, basename="resource")
urlpatterns = router.urls
