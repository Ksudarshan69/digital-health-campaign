from rest_framework.routers import DefaultRouter
from .api_views import NewsPostViewSet

router = DefaultRouter()
router.register("", NewsPostViewSet, basename="news-post")
urlpatterns = router.urls
