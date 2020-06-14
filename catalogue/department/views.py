import json
import logging

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView
from .forms import DepartmentForm
from .models import Department

UserModel = get_user_model()



""" Department View """
""""""""""""""""""""""""


def department_create(request, item=None):
    """
    Creates an department instance
    """
    form_class = DepartmentForm
    template_name = 'department/department-list.html'
    department_list = Department.objects.filter(enabled=True)
    msg = ""

    if request.method == "POST":
        department_form = form_class(request.POST, prefix='department', instance=item, request=request,)
        if department_form.is_valid():
            #department = department_form.save(commit=False)
            department = department_form.save()
            # msg = UPDATE_SUCCESS.format(department._meta.verbose_name, department) if item else CREATE_SUCCESS.format(
                                # department._meta.verbose_name, department)
            return redirect(Department.get_list_url())
        else:
            logging.warning("Department Form: {}".format(json.dumps(department_form.errors)))
            messages.warning(request, "Errrorr", "Error")
    else:
        department_form = form_class(prefix='department', instance=item, request=request)
    return render(request, template_name, {'department_form':department_form, 'departments': department_list})

def department_update(request, pk):
    """
    Edits an Department instance
    """
    return department_create(request, get_object_or_404(Department, pk=pk))

def department_delete(request, pk):
    """
    Deletes an Department instance
    """
    item = get_object_or_404(Contact, pk=pk)
    # msg = DELETE_SUCCESS.format(item._meta.verbose_name, item)
    item.delete()

    # if request.is_ajax():
    #     return JsonResponse({"msg": msg, "type": TYPE_SUCCESS}, safe=True)
    # else:
    #     messages.warning(request, msg, TITLE_SUCCESS)
    return redirect(Department.get_list_url())

def department_detail(request, pk):
    """
    Returns an department instance
    """
    instance = get_object_or_404(Department, pk=pk)
    return render(request, 'department/department-detail.html', context={'instance':instance})

def department_list(request, page=1):
    """
    Lists all departments
    """
    departments = Department.objects.filter(enabled=True)
    return render(request, 'department/department-list.html', context ={'departments':departments, 'page':page})
