from django.urls import include, path
from .views import department_create, department_delete, department_detail, department_list, department_update, \
    staff_create, staff_delete, staff_detail, staff_list, staff_update

app_name = 'department'
urlpatterns = [
    path('departments/', include([ 
        path('', department_create, name='department-add'),
        path('', department_list, name='department-list'),
        path('<uuid:pk>', department_update, name='department-edit'),
        path('<uuid:pk>', department_delete, name='department-delete'),
        path('<uuid:pk>', department_detail, name='department-detail'),
    ])),
    
    path('staff/', include([
        path('', staff_create, name='staff-add'),
        path('', staff_list, name='staff-list'),
        path('<uuid:pk>', staff_update, name='staff-edit'),
        path('<uuid:pk>', staff_delete, name='staff-delete'),
        path('<uuid:pk>', staff_detail, name='staff-detail'),
    ])),

]