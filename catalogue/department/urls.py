from django.urls import path
from .views import department_create, department_delete, department_detail, department_list, department_update

app_name = 'department'
urlpatterns = [
    path('departments/', department_create, name='department-add'),
    path('departments/', department_list, name='department-list'),
    path('departments/<uuid:pk>', department_update, name='department-edit'),
    path('departments/<uuid:pk>', department_delete, name='department-delete'),
    path('departments/<uuid:pk>', department_detail, name='department-detail'),

]