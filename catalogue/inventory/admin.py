from django.contrib import admin
from .models import Asset, Category

class AssetAdmin(admin.ModelAdmin):
    field = '__all__'

class CategoryAdmin(admin.ModelAdmin):
    field = '__all__'

admin.site.register(Asset, AssetAdmin)
admin.site.register(Category, CategoryAdmin)