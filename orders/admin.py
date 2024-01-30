from django.contrib import admin
from .models import Order, OrderDetail, Cart


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('user', 'order_date', 'total_amount')
    search_fields = ('user__username',)


class OrderDetailAdmin(admin.ModelAdmin):
    model = OrderDetail
    list_display = ('get_username', 'get_product_name', 'quantity', 'subtotal')
    search_fields = ('order__user__username', 'product__name')

    def get_username(self, obj):
        return obj.order.user.username

    get_username.short_description = 'Username'

    def get_product_name(self, obj):
        return obj.product.name

    get_product_name.short_description = 'Product'


class CartAdmin(admin.ModelAdmin):
    model = Cart
    list_display = ('user', 'product', 'quantity')
    search_fields = ('user__username', 'product__name')


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
admin.site.register(Cart, CartAdmin)
