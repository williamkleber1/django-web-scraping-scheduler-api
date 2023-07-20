from rest_framework import routers

from .views import AutomationViewSet, ScraperRobotViewSet, ExecutionLogViewSet

router = routers.DefaultRouter()
router.register(r'automations', AutomationViewSet)
router.register(r'scraper-robots', ScraperRobotViewSet)
router.register(r'execution-logs', ExecutionLogViewSet)
