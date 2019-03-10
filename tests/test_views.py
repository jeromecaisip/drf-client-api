from django.test import TestCase
from api_clients.models import Client
from django.urls import reverse
from rest_framework.test import APIClient


class APITestCase(TestCase):

    def setUp(self):
        self.client_object = Client.objects.create(api_key='test_api_key', name='test_client')
        self.authenticated_api_client = APIClient()
        self.unauthenticated_api_client = APIClient()

    def test_authenticated_access(self):
        self.authenticated_api_client.credentials(HTTP_API_KEY='test_api_key')
        response = self.authenticated_api_client.get(reverse("test-view"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["msg"], "Hello World!")

        response = self.authenticated_api_client.post(reverse("test-view"), data={'message': 'Test post'},
                                                      format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["msg"], "Test post")


