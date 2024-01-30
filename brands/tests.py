from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from brands.models import Brand


class BrandTests(APITestCase):

    def setUp(self):
        self.brand = Brand.objects.create(name='Realme')

    # create
    def test_create_brand(self):
        url = reverse('brands-list')
        data = {'name': 'HTC'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Brand.objects.count(), 2)
        brands = Brand.objects.all()
        self.assertEqual(brands[1].name, 'HTC')

    # get all
    def test_get_brands(self):
        response = self.client.get('/brands/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    # update
    def test_update_brand(self):
        url = reverse('brands-detail', args=[self.brand.id])
        data = {'name': 'Updated HTC'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Brand.objects.get(id=self.brand.id).name,
                         'Updated HTC')

    # delete
    def test_delete_brand(self):
        url = reverse('brands-detail', args=[self.brand.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Brand.objects.count(), 0)
