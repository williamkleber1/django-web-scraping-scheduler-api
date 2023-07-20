from rest_framework import serializers
from .models import Automation, ScraperRobot, ExecutionLog

class AutomationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Automation
        fields = '__all__'

class ScraperRobotSerializer(serializers.ModelSerializer):
    # automations = AutomationSerializer(many=True)
    class Meta:
        model = ScraperRobot
        fields = ['id', 'name', 'description', 'automations']

class ExecutionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecutionLog
        fields = '__all__'
