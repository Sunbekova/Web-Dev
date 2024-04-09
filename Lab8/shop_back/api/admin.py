from django.contrib import admin
from api.models import Product, Category




# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    
admin.site.register(Category)
