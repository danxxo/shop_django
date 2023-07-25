from django.contrib import admin
from .models import Category, Product, UploadedCSV

#log_admin

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        'price',
        'available',
        'consumer_profile',
        'created',
        'updated'
    ]
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(UploadedCSV)
class CSVAdmin(admin.ModelAdmin):
    list_display = [
        'consumer',
        'csv'
    ]

