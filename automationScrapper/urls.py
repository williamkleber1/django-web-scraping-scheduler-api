from rest_framework import routers

from .views import AutomationViewSet, ScrapperRobotViewSet, ExecutionLogViewSet

router = routers.DefaultRouter()
router.register(r'automations', AutomationViewSet)
router.register(r'scraper-robots', ScrapperRobotViewSet)
router.register(r'execution-logs', ExecutionLogViewSet)
