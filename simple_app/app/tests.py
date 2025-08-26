from django.test import TestCase
from django.urls import reverse
# Create your tests here.
class SimpleTest(TestCase):
    def test_api_endpoint(self):
        response = self.client.get(reverse('api_endpoint'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json())
