from rest_framework import serializers
from .models import Automation, ScrapperRobot, ExecutionLog

class AutomationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Automation
        fields = '__all__'

class ScrapperRobotSerializer(serializers.ModelSerializer):
    # automations = AutomationSerializer(many=True)
    class Meta:
        model = ScrapperRobot
        fields = ['id', 'name', 'description']

class ExecutionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecutionLog
        fields = '__all__'
