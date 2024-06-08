from django.contrib import admin

from .models import *

# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    # list_display = ['id', 'title']
    search_fields =  ['id', 'title']