from django.contrib import admin
from .models import Category, unit, Item, Supplier, Order

# Register your models here.
admin.site.register(Category)
admin.site.register(unit)
admin.site.register(Item)
admin.site.register(Supplier)
admin.site.register(Order)

