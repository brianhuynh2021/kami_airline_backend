from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class AirplaneViewTest(APITestCase):

    def test_valid_input_multiple_airplanes(self):
        url = reverse('airplane-api')
        data = [{'id': 1, 'passengers': 50}, {'id': 2, 'passengers': 60}]
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_exceeding_max_airplanes_limit(self):
        url = reverse('airplane-api')
        data = [{'id': i, 'passengers': 50} for i in range(1, 12)]
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Maximum of 10 airplanes allowed per request', response.data['message'])

    def test_invalid_airplane_data(self):
        url = reverse('airplane-api')
        data = [{'id': 1, 'passengers': -5}]
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    
        first_error = response.data[0]
        self.assertIn('passengers', first_error)
        self.assertIn('Number of passengers cannot be negative.', first_error['passengers'][0])

