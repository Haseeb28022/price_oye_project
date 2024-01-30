from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from accounts.models import CustomUser
from payments.models import Payment, Invoice
from orders.models import Order


class PaymentTests(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(username='abdulhaseeb',
                                              first_name='abdul',
                                              last_name='haseeb',
                                              email='haseeb.irfan28@gmail.com',
                                              password='12345678')
        self.payment = Payment.objects.create(amount='8000',
                                              success=True,
                                              payment_method="card",
                                              user=self.user)
        self.order = Order.objects.create(total_amount='100000',
                                          user=self.user)
        self.invoice = Invoice.objects.create(order=self.order,
                                              amount='8000',
                                              payment=self.payment)

    # ------ Payments ------
    # create
    def test_create_payment(self):
        url = reverse('payments-list')
        data = {'amount': '6500',
                'success': True,
                'payment_method': "card",
                'user': self.user.id}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Payment.objects.count(), 2)
        payments = Payment.objects.all()
        self.assertEqual(payments[1].amount, 6500)

    # get all
    def test_get_payment(self):
        response = self.client.get(reverse('payments-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    # update
    def test_update_payment(self):
        url = reverse('payments-detail', args=[self.payment.id])
        data = {'amount': '1000'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Payment.objects.get(id=self.payment.id).amount,
                         1000)

    # delete
    def test_delete_payment(self):
        url = reverse('payments-detail', args=[self.payment.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Payment.objects.count(), 0)

    # ------ Invoices ------
    # create
    def test_create_invoice(self):
        url = reverse('invoices-list')
        data = {'order': self.order.id,
                'amount': '21000',
                'payment': self.payment.id}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 2)
        invoice = Invoice.objects.all()
        self.assertEqual(invoice[1].amount, 21000)

    # get all
    def test_get_invoice(self):
        response = self.client.get(reverse('invoices-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    # update
    def test_update_invoice(self):
        url = reverse('invoices-detail', args=[self.invoice.id])
        data = {'amount': '8100'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Invoice.objects.get(id=self.invoice.id).amount,
                         8100)

    # delete
    def test_delete_invoice(self):
        url = reverse('invoices-detail', args=[self.invoice.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Invoice.objects.count(), 0)
