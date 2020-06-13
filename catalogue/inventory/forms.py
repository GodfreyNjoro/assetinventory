from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from .models import Asset, Category

UserModel = get_user_model()

class AssetForm(ModelForm):
    def __init__(self, *args, request, **kwargs):
        super(AssetForm, self).__init__(*args, **kwargs)  # populates the post
        self.fields['description'].widget.attrs = {'class' : 'form-control', 'rows': 2}
        self.fields['purchase_date'].widget.attrs = {'class': 'form-control', 'data-type': 'date', 'placeholder': 'Purchase Date', 'title': 'Date asset was purchased'}
        self.fields["category"].widget.attrs = {'class': 'form-control select2-single'}
        self.fields['cost'].widget.attrs = {'class':'form-control', 'title':'Cost of the asset'}
        self.fields["category"].queryset = Category.objects.filter(enabled=True)

    
    class Meta:
        model = Asset
        exclude = ('enabled', 'created', 'updated', 'is_active', )



class CategoryForm(ModelForm):
    def __init__(self, *args, request, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)  # populates the post
    
    class Meta:
        model = Category
        exclude = ('enabled', 'created', 'updated', 'is_active', )
