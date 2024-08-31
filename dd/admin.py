from django.contrib import admin
from .models import Customer,Inventory,Transaction,Order
# Register your models here.

admin.site.register(Customer)
admin.site.register(Inventory)
admin.site.register(Transaction)
admin.site.register(Order)

