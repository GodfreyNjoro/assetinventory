from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from .models import Department

UserModel = get_user_model()

class DepartmentForm(ModelForm):
    def __init__(self, *args, request, **kwargs):
        self.request = kwargs.pop('request', None)
        super(DepartmentForm, self).__init__(*args, **kwargs)  # populates the post
        

    
    class Meta:
        model = Department
        fields = ('name',)
