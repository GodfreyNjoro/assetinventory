from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from .models import Asset, AssetCategory

UserModel = get_user_model()

class AssetForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AssetForm, self).__init__(*args, **kwargs)  # populates the post
        self.fields['description'].widget.attrs = {'class' : 'form-control', 'rows': 2}
        self.fields["category"].queryset = AssetCategory.objects.filter(enabled=True)

    
    class Meta:
        model = Asset
        exclude = ('enabled', 'created', 'updated', 'is_active', )



class AssetCategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AssetCategoryForm, self).__init__(*args, **kwargs)  # populates the post
    
    class Meta:
        model = AssetCategory
        exclude = ('enabled', 'created', 'updated', 'is_active', )
