# test_automation.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from automationScrapper.models import Automation, ScrapperRobot
import datetime

class AutomationViewSetTest(APITestCase):
    def setUp(self):
        self.list_url = reverse('automation-list')
        self.robot = ScrapperRobot.objects.create(name='Test Robot', description='Test Description')
        # Use datetime.time para criar o objeto scheduled_time
        self.automation = Automation.objects.create(
            id_scraper_robot=self.robot,
            url='https://example.com/api/',
            http_method='GET',
            request_body='',
            scheduled_time=datetime.time(12, 0, 0),  # Use o construtor datetime.time para definir a hora
            scheduled_frequency='Hourly',
        )

    def test_create_automation(self):
        data = {
            'id_scraper_robot': self.robot.id,
            'url': 'https://example2.com/api/',
            'http_method': 'GET',
            'request_body': '',
            'scheduled_time': '12:00:00',
            'scheduled_frequency': 'Hourly',
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Automation.objects.count(), 2)
        self.assertEqual(Automation.objects.get(pk=response.data['id']).url, 'https://example2.com/api/')

    def test_list_automations(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_retrieve_automation(self):
        detail_url = reverse('automation-detail', kwargs={'pk': self.automation.id})
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['url'], 'https://example.com/api/')

    def test_update_automation(self):
        detail_url = reverse('automation-detail', kwargs={'pk': self.automation.id})
        data = {
            'url': 'https://example.com/updated-api/',
            'http_method': 'POST',
            'scheduled_time': '14:00:00',  # Adicione o campo scheduled_time na atualização
            'scheduled_frequency': 'Daily',  # Adicione o campo scheduled_frequency na atualização
        }
        response = self.client.patch(detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verifique se os campos foram atualizados corretamente no banco de dados
        self.automation.refresh_from_db()
        self.assertEqual(self.automation.url, 'https://example.com/updated-api/')
        self.assertEqual(self.automation.http_method, 'POST')
        self.assertEqual(self.automation.scheduled_time, datetime.time(14, 0, 0))
        self.assertEqual(self.automation.scheduled_frequency, 'Daily')

    def test_delete_automation(self):
        detail_url = reverse('automation-detail', kwargs={'pk': self.automation.id})
        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Automation.objects.count(), 0)
