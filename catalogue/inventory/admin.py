from django.contrib import admin
from .models import Asset, AssetCategory

class AssetAdmin(admin.ModelAdmin):
    field = '__all__'

class AssetCategoryAdmin(admin.ModelAdmin):
    field = '__all__'

admin.site.register(Asset, AssetAdmin)
admin.site.register(AssetCategory, AssetCategoryAdmin)