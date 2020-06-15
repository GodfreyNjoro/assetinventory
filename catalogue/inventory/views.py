import json
import logging

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView
from .forms import AssetForm, CategoryForm
from .models import Asset, Category

UserModel = get_user_model()



""" Asset View """
""""""""""""""""""


def asset_create(request, item=None):
    """
    Creates an Asset instance
    """
    form_class = AssetForm
    template_name = 'inventory/asset-list.html'
    asset_list = Asset.objects.filter(enabled=True)
    msg = ""

    if request.method == "POST":
        asset_form = form_class(request.POST, prefix='asset', instance=item, request=request,)
        if asset_form.is_valid():
            #asset = asset_form.save(commit=False)
            asset = asset_form.save()
            # msg = UPDATE_SUCCESS.format(asset._meta.verbose_name, asset) if item else CREATE_SUCCESS.format(
                                # asset._meta.verbose_name, asset)
            return redirect(Asset.get_list_url())
        else:
            logging.warning("Asset Form: {}".format(json.dumps(asset_form.errors)))
            messages.warning(request, "Errrorr", "Error")
    else:
        asset_form = form_class(prefix='asset', instance=item, request=request)
    return render(request, template_name, {'asset_form':asset_form, 'assets': asset_list})

def asset_update(request, pk):
    """
    Edits an Asset instance
    """
    return asset_create(request, get_object_or_404(Asset, pk=pk))

def asset_delete(request, pk):
    """
    Deletes an Asset instance
    """
    item = get_object_or_404(Asset, pk=pk)
    # msg = DELETE_SUCCESS.format(item._meta.verbose_name, item)
    item.delete()

    # if request.is_ajax():
    #     return JsonResponse({"msg": msg, "type": TYPE_SUCCESS}, safe=True)
    # else:
    #     messages.warning(request, msg, TITLE_SUCCESS)
    return redirect(Asset.get_list_url())

def asset_detail(request, pk):
    """
    Returns an Asset instance
    """
    instance = get_object_or_404(Asset, pk=pk)
    return render(request, 'inventory/asset-detail.html', context={'instance':instance})

def asset_list(request, page=1):
    """
    Lists all assets
    """
    assets = Asset.objects.filter(enabled=True)
    return render(request, 'inventory/asset-list.html', context ={'assets':assets, 'page':page})


""" Category View """
""""""""""""""""""""""""


def category_create(request, item=None):
    """
    Creates a Category instance
    """
    form_class = CategoryForm
    template_name = 'inventory/category-list.html'
    category_list = Category.objects.filter(enabled=True)
    msg = ""

    if request.method == "POST":
        category_form = form_class(request.POST, prefix='category', instance=item, request=request,)
        if category_form.is_valid():
            #asset = category_form.save(commit=False)
            category = category_form.save()
            # msg = UPDATE_SUCCESS.format(asset._meta.verbose_name, asset) if item else CREATE_SUCCESS.format(
                                # asset._meta.verbose_name, asset)
            return redirect(Category.get_list_url())
        else:
            logging.warning("Category Form: {}".format(json.dumps(category_form.errors)))
            messages.warning(request, "Errrorr", "Error")
    else:
        category_form = form_class(prefix='category', instance=item, request=request)
    return render(request, template_name, {'category_form':category_form, 'categories': category_list})

def category_update(request, pk):
    """
    Edits a Category instance
    """
    return category_create(request, get_object_or_404(Category, pk=pk))

def category_delete(request, pk):
    """
    Deletes a Category instance
    """
    item = get_object_or_404(Category, pk=pk)
    # msg = DELETE_SUCCESS.format(item._meta.verbose_name, item)
    item.delete()

    # if request.is_ajax():
    #     return JsonResponse({"msg": msg, "type": TYPE_SUCCESS}, safe=True)
    # else:
    #     messages.warning(request, msg, TITLE_SUCCESS)
    return redirect(Category.get_list_url())

def category_detail(request, pk):
    """
    Returns a Category instance
    """
    instance = get_object_or_404(Category, pk=pk)
    return render(request, 'inventory/category-detail.html', context={'instance':instance})

def category_list(request, page=1):
    """
    Lists all categories
    """
    categories = Category.objects.filter(enabled=True)
    return render(request, 'inventory/category-list.html', context ={'assets':categories, 'page':page})

