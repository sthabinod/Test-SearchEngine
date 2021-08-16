from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone')
    search_fields = ('phone',)

    list_per_page = 4
