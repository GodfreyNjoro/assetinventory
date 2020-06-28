from django.urls import include, path
from .views import *

app_name = 'location'
urlpatterns = [
    path('sites/', include([
        path('', site_create, name='site-add'),
        path('', site_list, name='site-list'),
        path('<uuid:pk>', site_update, name='site-edit'),
        path('<uuid:pk>', site_delete, name='site-delete'),
        path('<uuid:pk>', site_detail, name='site-detail'),
    ])),
    path('locations/', include([
        path('', location_create, name='location-add'),
        path('', location_list, name='location-list'),
        path('<uuid:pk>', location_update, name='location-edit'),
        path('<uuid:pk>', location_delete, name='location-delete'),
        path('<uuid:pk>', location_detail, name='location-detail'),
    ])),
]