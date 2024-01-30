from django.db import models
from accounts.models import CustomUser
from orders.models import Order


class Payment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField(default=False)
    payment_method = models.CharField(
        max_length=50,
        default='cash'
    )  # additional added


class Invoice(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment = models.ForeignKey(
        Payment,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
