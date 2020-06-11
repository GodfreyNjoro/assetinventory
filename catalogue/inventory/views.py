from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .forms import AssetForm, AssetCategoryForm
from .models import Asset, AssetCategory

UserModel = get_user_model()

class AssetView(View):
    form_class = AssetForm
    template_name = 'inventory/asset_list.html'
    asset_list = Asset.objects.filter(enabled=True)
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form':form, 'asset_list': self.asset_list})

    def post(self, request, *args, **kwargs):
        pass


class AssetList(ListView):
    context_object_name = 'asset_list'
    queryset = Asset.objects.filter(enabled=True)
    template_name = 'inventory/asset_list.html'