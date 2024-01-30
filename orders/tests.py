from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from accounts.models import CustomUser
from orders.models import Order, OrderDetail, Cart
from shop.models import Product
from brands.models import Brand
from categories.models import Category


class OrderTests(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(username='abdulhaseeb',
                                              first_name='abdul',
                                              last_name='haseeb',
                                              email='haseeb.irfan28@gmail.com',
                                              password='12345678')
        self.order = Order.objects.create(total_amount='100000',
                                          user=self.user)
        self.brand = Brand.objects.create(name='Realme')
        self.category = Category.objects.create(name='Tablets')
        self.product = Product.objects.create(name='Samsung S22',
                                              description='Samsung S22 mobile',
                                              price='200000',
                                              stock_quantity=5,
                                              brand=self.brand,
                                              category=self.category)
        self.order_detail = OrderDetail.objects.create(order=self.order,
                                                       product=self.product,
                                                       quantity=10,
                                                       subtotal='500000')
        self.cart = Cart.objects.create(user=self.user,
                                        product=self.product,
                                        quantity=20)

    # ------ Order ------
    # create
    def test_create_order(self):
        url = reverse('orders-list')
        data = {'total_amount': '50000',
                'user': self.user.id}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 2)
        orders = Order.objects.all()
        self.assertEqual(orders[1].total_amount, 50000)

    # get all
    def test_get_order(self):
        response = self.client.get('/orders/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    # update
    def test_update_order(self):
        url = reverse('orders-detail', args=[self.order.id])
        data = {'total_amount': '100'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Order.objects.get(id=self.order.id).total_amount,
                         100)

    # delete
    def test_delete_order(self):
        url = reverse('orders-detail', args=[self.order.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Order.objects.count(), 0)

    # ------ order details ------
    # create
    def test_create_order_detail(self):
        url = reverse('orderDetails-list')
        data = {'order': self.order.id,
                'product': self.product.id,
                'quantity': 5,
                'subtotal': '10'}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(OrderDetail.objects.count(), 2)
        order_detail = OrderDetail.objects.all()
        self.assertEqual(order_detail[1].subtotal, 10)

    # get all
    def test_get_order_detail(self):
        response = self.client.get('/order_details/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    # update
    def test_update_order_detail(self):
        url = reverse('orderDetails-detail', args=[self.order_detail.id])
        data = {'quantity': '6'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(OrderDetail.objects.get(id=self.order_detail.id)
                         .quantity, 6)

    # delete
    def test_delete_order_detail(self):
        url = reverse('orderDetails-detail', args=[self.order_detail.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(OrderDetail.objects.count(), 0)

    # ------ cart ------
    # create
    def test_create_cart(self):
        url = reverse('cart-list')
        data = {'user': self.user.id,
                'product': self.product.id,
                'quantity': 5}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cart.objects.count(), 2)
        cart = Cart.objects.all()
        self.assertEqual(cart[1].quantity, 5)

    # get all
    def test_get_cart(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    # update
    def test_update_cart(self):
        url = reverse('cart-detail', args=[self.cart.id])
        data = {'quantity': '2'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Cart.objects.get(id=self.cart.id)
                         .quantity, 2)

    # delete
    def test_delete_cart(self):
        url = reverse('cart-detail', args=[self.cart.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Cart.objects.count(), 0)
