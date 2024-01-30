from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


# Register the Category model with its custom admin class
admin.site.register(Category, CategoryAdmin)
