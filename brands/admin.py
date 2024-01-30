from django.contrib import admin
from .models import Brand


class BrandAdmin(admin.ModelAdmin):
    model = Brand
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


# Register the Brand model with its custom admin class
admin.site.register(Brand, BrandAdmin)
