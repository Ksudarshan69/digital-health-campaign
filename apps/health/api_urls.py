from rest_framework.routers import DefaultRouter
from .api_views import HealthToolViewSet

router = DefaultRouter()
router.register("", HealthToolViewSet, basename="health-tool")
urlpatterns = router.urls
