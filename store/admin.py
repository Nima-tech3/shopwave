from django.contrib import admin
from .models import Category, Product

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'status', 'price']
    ordering = ['name', 'created']
    list_filter = ['status', 'created', 'category']
    search_fields = ['name', 'description']
    raw_id_fields = ['category']
    date_hierarchy = 'created'
    prepopulated_fields = {"slug": ['name']}
    list_editable = ['status', 'price']
    