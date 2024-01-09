from rest_framework_nested import routers
from . import views

# URLConf
router = routers.DefaultRouter()
router.register("bloggers", views.BloggerViewSet)
urlpatterns = router.urls
