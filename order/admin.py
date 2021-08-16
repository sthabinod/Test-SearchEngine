from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('phone', 'order_address', 'order_date', 'order_status')
    search_fields = ('phone', 'order_status', 'order_date')
    autocomplete_fields = ('product',)
    list_per_page = 4
