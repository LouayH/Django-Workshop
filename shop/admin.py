from django.contrib import admin
from . import models

# Register your models here.
admin.site.site_header = "Coretabs"
admin.site.index_title = "Coretabs Online Shop"
admin.site.site_title = "Administration"

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    search_fields = ['name']
    list_display = ('name', 'description',)

def zerofy(modeladmin, request, queryset):
    queryset.update(price=0)

zerofy.short_description = "Zerofy selected products"

def discount(modeladmin, request, queryset):
    for product in queryset:
        product.price = product.price * 80 / 100
        product.save()

discount.short_description = "20 percent discount selected products"

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    search_fields = ['name']
    list_display = ('name', 'price', 'stock', 'category',)
    list_filter = ('created_at', 'category',)
    actions = [zerofy, discount]