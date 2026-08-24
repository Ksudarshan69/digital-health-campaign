from rest_framework.routers import DefaultRouter
from .api_views import PreventiveHealthTopicViewSet

router = DefaultRouter()
router.register("", PreventiveHealthTopicViewSet, basename="preventive-topic")
urlpatterns = router.urls
