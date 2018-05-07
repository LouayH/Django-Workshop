from django.contrib import admin
from . import models

# Register your models here.
admin.site.site_header = "Coretabs"
admin.site.index_title = "Coretabs Online Shop"
admin.site.site_title = "Administration"

admin.site.register(models.Category)

def zerofy(modeladmin, request, queryset):
    queryset.update(price=0)

zerofy.short_description = "Zerofy selected products"

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    search_fields = ['name']
    list_display = ('name', 'price', 'stock', 'category',)
    list_filter = ('created_at', 'category',)
    actions = [zerofy]