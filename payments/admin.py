from django.contrib import admin
from .models import Payment, Invoice


class PaymentAdmin(admin.ModelAdmin):
    model = Payment
    list_display = ('user', 'amount', 'timestamp', 'success', 'payment_method')
    search_fields = ('user__username',)
    list_filter = ('success', 'payment_method')


class InvoiceAdmin(admin.ModelAdmin):
    model = Invoice
    list_display = ('order', 'amount', 'payment')
    search_fields = ('order__user__username',)
    list_filter = ('order__user',)


admin.site.register(Payment, PaymentAdmin)
admin.site.register(Invoice, InvoiceAdmin)
