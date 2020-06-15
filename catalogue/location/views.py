import json
import logging

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView
from .forms import LocationForm, SiteForm
from .models import Location, Site

UserModel = get_user_model()



""" Site View """
""""""""""""""""""


def site_create(request, item=None):
    """
    Creates an Site instance
    """
    form_class = SiteForm
    template_name = 'location/site-list.html'
    site_list = Site.objects.filter(enabled=True)
    msg = ""

    if request.method == "POST":
        site_form = form_class(request.POST, prefix='site', instance=item, request=request,)
        if site_form.is_valid():
            #site = site_form.save(commit=False)
            site = site_form.save()
            # msg = UPDATE_SUCCESS.format(site._meta.verbose_name, site) if item else CREATE_SUCCESS.format(
                                # site._meta.verbose_name, site)
            return redirect(Site.get_list_url())
        else:
            logging.warning("Site Form: {}".format(json.dumps(site_form.errors)))
            messages.warning(request, "Errrorr", "Error")
    else:
        site_form = form_class(prefix='site', instance=item, request=request)
    return render(request, template_name, {'site_form':site_form, 'sites': site_list})

def site_update(request, pk):
    """
    Edits an Site instance
    """
    return site_create(request, get_object_or_404(Site, pk=pk))

def site_delete(request, pk):
    """
    Deletes an Site instance
    """
    item = get_object_or_404(Site, pk=pk)
    # msg = DELETE_SUCCESS.format(item._meta.verbose_name, item)
    item.delete()

    # if request.is_ajax():
    #     return JsonResponse({"msg": msg, "type": TYPE_SUCCESS}, safe=True)
    # else:
    #     messages.warning(request, msg, TITLE_SUCCESS)
    return redirect(Site.get_list_url())

def site_detail(request, pk):
    """
    Returns an Site instance
    """
    instance = get_object_or_404(Site, pk=pk)
    return render(request, 'location/site-detail.html', context={'instance':instance})

def site_list(request, page=1):
    """
    Lists all sites
    """
    sites = Site.objects.filter(enabled=True)
    return render(request, 'location/site-list.html', context ={'sites':sites, 'page':page})


""" Location View """
""""""""""""""""""""""""


def location_create(request, item=None):
    """
    Creates a Location instance
    """
    form_class = LocationForm
    template_name = 'location/location-list.html'
    location_list = Location.objects.filter(enabled=True)
    msg = ""

    if request.method == "POST":
        location_form = form_class(request.POST, prefix='location', instance=item, request=request,)
        if location_form.is_valid():
            #site = location_form.save(commit=False)
            location = location_form.save()
            # msg = UPDATE_SUCCESS.format(site._meta.verbose_name, site) if item else CREATE_SUCCESS.format(
                                # site._meta.verbose_name, site)
            return redirect(Location.get_list_url())
        else:
            logging.warning("Location Form: {}".format(json.dumps(location_form.errors)))
            messages.warning(request, "Errrorr", "Error")
    else:
        location_form = form_class(prefix='location', instance=item, request=request)
    return render(request, template_name, {'location_form':location_form, 'locations': location_list})

def location_update(request, pk):
    """
    Edits a Location instance
    """
    return location_create(request, get_object_or_404(Location, pk=pk))

def location_delete(request, pk):
    """
    Deletes a Location instance
    """
    item = get_object_or_404(Location, pk=pk)
    # msg = DELETE_SUCCESS.format(item._meta.verbose_name, item)
    item.delete()

    # if request.is_ajax():
    #     return JsonResponse({"msg": msg, "type": TYPE_SUCCESS}, safe=True)
    # else:
    #     messages.warning(request, msg, TITLE_SUCCESS)
    return redirect(Location.get_list_url())

def location_detail(request, pk):
    """
    Returns an Location instance
    """
    instance = get_object_or_404(Location, pk=pk)
    return render(request, 'location/location-detail.html', context={'instance':instance})

def location_list(request, page=1):
    """
    Lists all locations
    """
    locations = Location.objects.filter(enabled=True)
    return render(request, 'location/location-list.html', context ={'locations':locations, 'page':page})

