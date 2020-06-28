from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from .models import Site, Location

UserModel = get_user_model()

class SiteForm(ModelForm):
    def __init__(self, *args, request, **kwargs):
        super(SiteForm, self).__init__(*args, **kwargs)  # populates the post
        self.fields['description'].widget.attrs = {'class' : 'form-control', 'rows': 2}

    
    class Meta:
        model = Site
        exclude = ('enabled', 'created', 'updated', 'is_active', )



class LocationForm(ModelForm):
    def __init__(self, *args, request, **kwargs):
        super(LocationForm, self).__init__(*args, **kwargs)  # populates the post
        self.fields["site"].widget.attrs = {'class': 'form-control select2-single'}
        self.fields["site"].queryset = Site.objects.filter(enabled=True)

    
    class Meta:
        model = Location
        exclude = ('enabled', 'created', 'updated', 'is_active', )
