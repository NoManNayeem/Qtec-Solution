from .models import Product



from django.contrib import admin
from django.contrib import admin
from .models import Category, Brand, Warranty, Seller, Product

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Warranty)
admin.site.register(Seller)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',"category","brand",'warranty','price',)
    list_filter = ('name',"category","brand",'warranty','price',)
     

