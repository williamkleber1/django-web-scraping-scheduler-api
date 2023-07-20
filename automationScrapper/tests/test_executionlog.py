# test_executionlog.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from automationScrapper.models import ExecutionLog, Automation, ScrapperRobot
from django.utils import timezone
import datetime
import time
from django_celery_beat.models import CrontabSchedule, PeriodicTask

class ExecutionLogViewSetTest(APITestCase):
    def setUp(self):
        self.list_url = reverse('executionlog-list')
        self.robot = ScrapperRobot.objects.create(name='Test Robot', description='Test Description')
        now = timezone.now()
        scheduled_time = now + datetime.timedelta(minutes=1)
        self.automation = Automation.objects.create(
            id_scraper_robot=self.robot,
            url='https://example.com/api/',
            http_method='GET',
            request_body='',
            scheduled_time=scheduled_time.time(),
            scheduled_frequency='Hourly',
        )
        print("Waiting 2 minutes before continuing...")
        # Espere 2 minutos (120 segundos) antes de continuar
        #time.sleep(120)

    def test_create_execution_log(self):
        self.assertEqual(PeriodicTask.objects.count(), 1)
        