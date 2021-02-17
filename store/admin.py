from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class Admin(admin.ModelAdmin):
    list_display = ['name', 'slug']
