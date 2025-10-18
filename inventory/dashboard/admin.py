from django.contrib import admin
from .models import product,Order
from django.contrib.auth.models import Group
admin.site.site_header = 'RobInventory Dashboard'
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category','Quantity')
    list_filter = ('category',)
# Register your models here.
admin.site.register(product, ProductAdmin)
admin.site.register(Order)


