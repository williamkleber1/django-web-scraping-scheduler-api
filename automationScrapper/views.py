from rest_framework import viewsets
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Automation, ScraperRobot, ExecutionLog
from .serializers import (
    AutomationSerializer,
    ScraperRobotSerializer,
    ExecutionLogSerializer,
)

class AutomationViewSet(viewsets.ModelViewSet):
    queryset = Automation.objects.all()
    serializer_class = AutomationSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['url', 'http_method', 'scheduled_frequency', 'scheduled_time']

class ScraperRobotFilter(filters.FilterSet):
    description_contains = filters.CharFilter(field_name='description', lookup_expr='icontains')

    class Meta:
        model = ScraperRobot
        fields = []

class ScraperRobotViewSet(viewsets.ModelViewSet):
    queryset = ScraperRobot.objects.all()
    serializer_class = ScraperRobotSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = ScraperRobotFilter

class ExecutionLogViewSet(viewsets.ModelViewSet):
    queryset = ExecutionLog.objects.all()
    serializer_class = ExecutionLogSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['automation', 'automation__scheduled_time', 'automation__http_method', 'status_code']
