
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from automationScrapper.models import ScrapperRobot


class ScrapperRobotViewSetTest(APITestCase):
    def setUp(self):
        self.list_url = reverse('scrapperrobot-list')
        ScrapperRobot.objects.create(name='Robot1', description='Description1')
        ScrapperRobot.objects.create(name='Robot2', description='Description2')

    def test_create_scrapper_robot(self):
        data = {
            'name': 'My Scrapper Robot',
            'description': 'A description for my scrapper robot.',
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ScrapperRobot.objects.count(), 3)
        self.assertEqual(ScrapperRobot.objects.get(
            pk=response.data['id']).name, 'My Scrapper Robot')

    def test_list_scrapper_robots(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_scrapper_robot(self):
        detail_url = reverse('scrapperrobot-detail',
                             kwargs={'pk': ScrapperRobot.objects.first().id})
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Robot1')

    def test_update_scrapper_robot(self):
        detail_url = reverse('scrapperrobot-detail',
                             kwargs={'pk': ScrapperRobot.objects.first().id})
        data = {
            'name': 'Updated Robot',
            'description': 'An updated description.',
        }
        response = self.client.put(detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        robot = ScrapperRobot.objects.first()
        self.assertEqual(robot.name, 'Updated Robot')
        self.assertEqual(robot.description, 'An updated description.')

    def test_delete_scrapper_robot(self):
        detail_url = reverse('scrapperrobot-detail',
                             kwargs={'pk': ScrapperRobot.objects.first().id})
        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ScrapperRobot.objects.count(), 1)
