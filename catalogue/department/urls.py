from django.urls import include, path
from .views import department_create, department_delete, department_detail, department_list, department_update

app_name = 'department'
urlpatterns = [
    path('departments/', include([ 
        path('', department_create, name='department-add'),
        path('', department_list, name='department-list'),
        path('<uuid:pk>', department_update, name='department-edit'),
        path('<uuid:pk>', department_delete, name='department-delete'),
        path('<uuid:pk>', department_detail, name='department-detail'),
    ])),

]