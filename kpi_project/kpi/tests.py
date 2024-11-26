from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status
from .models import KPI

class KPITests(APITestCase):
    def test_create_kpi(self):
        data = {'name': 'Test KPI', 'expression': 'ATTR + 10'}
        response = self.client.post('/api/kpi/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(KPI.objects.count(), 1)
        self.assertEqual(KPI.objects.get().name, 'Test KPI')

    def test_link_asset_to_kpi(self):
        kpi = KPI.objects.create(name='Test KPI', expression='ATTR + 10')
        data = {'kpi': kpi.id, 'asset_id': 123}
        response = self.client.post('/api/kpi/link/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
