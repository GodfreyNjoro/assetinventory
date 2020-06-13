from django.urls import path
from .views import *

app_name = 'inventory'
urlpatterns = [
    path('assets/', asset_create, name='asset-add'),
    path('assets/', asset_list, name='asset-list'),
    path('assets/<uuid:pk>', asset_update, name='asset-edit'),
    path('assets/<uuid:pk>', asset_delete, name='asset-delete'),
    path('assets/<uuid:pk>', asset_detail, name='asset-detail'),

    path('categories/', category_create, name='category-add'),
    path('categories/', category_list, name='category-list'),
    path('categories/<uuid:pk>', category_update, name='category-edit'),
    path('categories/<uuid:pk>', category_delete, name='category-delete'),
    path('categories/<uuid:pk>', category_detail, name='category-detail'),

]