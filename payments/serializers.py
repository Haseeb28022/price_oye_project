from rest_framework import serializers

from payments.models import Payment, Invoice


class InvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invoice
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    invoice = InvoiceSerializer(many=True, read_only=True,
                                source='invoice_set')

    class Meta:
        model = Payment
        fields = '__all__'
