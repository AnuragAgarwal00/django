from django.contrib import admin
from .models import Addresses

@admin.register(Addresses)
class AdminAddress(admin.ModelAdmin):
    list_display = ['user', 'street', 'pincode', 'country', 'state', 'phone_no']
    list_filter = ['state', 'country']
    search_fields = ('street', 'pincode')
