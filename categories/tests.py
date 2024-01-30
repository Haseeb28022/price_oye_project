from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from categories.models import Category


class CategoryTests(APITestCase):

    def setUp(self):
        self.Category = Category.objects.create(name='Tablets')

    # create
    def test_create_category(self):
        url = '/categories/'
        data = {'name': 'AC'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)
        Categorys = Category.objects.all()
        self.assertEqual(Categorys[1].name, 'AC')

    # get all
    def test_get_categorys(self):
        response = self.client.get('/categories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    # update
    def test_update_category(self):
        url = reverse('categories-detail', args=[self.Category.id])
        data = {'name': 'Updated Tablets'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.get(id=self.Category.id).name,
                         'Updated Tablets')

    # delete
    def test_delete_category(self):
        url = reverse('categories-detail', args=[self.Category.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)
