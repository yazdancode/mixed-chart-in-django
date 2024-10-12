from django.contrib import admin
from .models import Product, ProductSold

class Productadmin(admin.ModelAdmin):
    list_display = ("name",)

class ProductSoldadmin(admin.ModelAdmin):
    list_display =("product", "count", "sell_date_time", "monthdict", )


admin.site.register(Product,Productadmin)
admin.site.register(ProductSold,ProductSoldadmin)