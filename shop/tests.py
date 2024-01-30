from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from shop.models import Product
from brands.models import Brand
from categories.models import Category


class ProductTests(APITestCase):

    def setUp(self):
        self.brand = Brand.objects.create(name='Samsung')
        self.category = Category.objects.create(name='Mobile')
        self.product = Product.objects.create(name='Samsung S22',
                                              description='Samsung S22 mobile',
                                              price='200000',
                                              stock_quantity=5,
                                              brand=self.brand,
                                              category=self.category)

    # create
    def test_create_product(self):
        url = reverse('products-list')
        data = {'name': 'Samsung S22 pro',
                'description': 'Samsung S22 pro mobile',
                'price': '300000',
                'stock_quantity': 2,
                'brand': self.brand.id,
                'category': self.category.id}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)
        products = Product.objects.all()
        self.assertEqual(products[1].name, 'Samsung S22 pro')

    # get all
    def test_get_product(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    # update
    def test_update_product(self):
        url = reverse('products-detail', args=[self.product.id])
        data = {'price': '50000'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.get(id=self.product.id).price,
                         50000)

    # delete
    def test_delete_product(self):
        url = reverse('products-detail', args=[self.product.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)
