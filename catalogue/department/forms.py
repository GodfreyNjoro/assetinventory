from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from .models import Department, Staff
from location.models import Location

UserModel = get_user_model()

class DepartmentForm(ModelForm):
    def __init__(self, *args, request, **kwargs):
        self.request = kwargs.pop('request', None)
        super(DepartmentForm, self).__init__(*args, **kwargs)  # populates the post
        

    
    class Meta:
        model = Department
        fields = ('name',)

class StaffForm(ModelForm):
    def __init__(self, *args, request, **kwargs):
        super(StaffForm, self).__init__(*args, **kwargs)  # populates the post
        self.fields["department"].widget.attrs = {'class': 'form-control select2-single'}
        self.fields["location"].widget.attrs = {'class': 'form-control select2-single '}
        self.fields['notes'].widget.attrs = {'class' : 'form-control', 'rows': 2}
        self.fields["department"].queryset = Department.objects.filter(enabled=True)
        self.fields["location"].queryset = Location.objects.filter(enabled=True)

    
    class Meta:
        model = Staff
        exclude = ('enabled', 'created', 'updated', 'is_active', )