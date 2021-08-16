from django.contrib import admin
from .models import Information


@admin.register(Information)
class AdminInformation(admin.ModelAdmin):
    pass
