from rest_framework import viewsets
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Automation, ScrapperRobot, ExecutionLog
from .serializers import (
    AutomationSerializer,
    ScrapperRobotSerializer,
    ExecutionLogSerializer,
)

class AutomationViewSet(viewsets.ModelViewSet):
    queryset = Automation.objects.all()
    serializer_class = AutomationSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['url', 'http_method', 'scheduled_frequency', 'scheduled_time']

class ScrapperRobotFilter(filters.FilterSet):
    description_contains = filters.CharFilter(field_name='description', lookup_expr='icontains')

    class Meta:
        model = ScrapperRobot
        fields = []

class ScrapperRobotViewSet(viewsets.ModelViewSet):
    queryset = ScrapperRobot.objects.all()
    serializer_class = ScrapperRobotSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = ScrapperRobotFilter

class ExecutionLogViewSet(viewsets.ModelViewSet):
    queryset = ExecutionLog.objects.all()
    serializer_class = ExecutionLogSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['automation', 'automation__scheduled_time', 'automation__http_method', 'status_code']
