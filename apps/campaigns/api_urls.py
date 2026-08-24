from rest_framework.routers import DefaultRouter
from .api_views import CampaignAreaViewSet

router = DefaultRouter()
router.register("", CampaignAreaViewSet, basename="campaign-area")
urlpatterns = router.urls
