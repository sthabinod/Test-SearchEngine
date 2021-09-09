from django.contrib import admin
from .models import MoreAboutUser


@admin.register(MoreAboutUser)
class MoreAboutUserAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone')
    search_fields = ('phone',)

    list_per_page = 4
