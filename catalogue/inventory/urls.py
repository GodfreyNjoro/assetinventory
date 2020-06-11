from django.urls import path
from .views import AssetList, AssetView

app_name = 'inventory'
urlpatterns = [
    path('assets/', AssetView.as_view(), name='asset-list'),
    path('assets/', AssetList.as_view(), name='asset'),
]