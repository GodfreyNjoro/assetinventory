import json
import logging

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView
from .forms import DepartmentForm, StaffForm
from .models import Department, Staff

UserModel = get_user_model()



""" Department View """
""""""""""""""""""""""""


def department_create(request, item=None):
    """
    Creates an Department instance
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
    Returns an Department instance
    """
    instance = get_object_or_404(Department, pk=pk)
    return render(request, 'department/department-detail.html', context={'instance':instance})

def department_list(request, page=1):
    """
    Lists all departments
    """
    departments = Department.objects.filter(enabled=True)
    return render(request, 'department/department-list.html', context ={'departments':departments, 'page':page})




""" Staff View """
""""""""""""""""""


def staff_create(request, item=None):
    """
    Creates an Staff instance
    """
    form_class = StaffForm
    template_name = 'department/staff-list.html'
    staff_list = Staff.objects.filter(enabled=True)
    msg = ""

    if request.method == "POST":
        staff_form = form_class(request.POST, prefix='staff', instance=item, request=request,)
        if staff_form.is_valid():
            #staff = staff_form.save(commit=False)
            staff = staff_form.save()
            # msg = UPDATE_SUCCESS.format(staff._meta.verbose_name, staff) if item else CREATE_SUCCESS.format(
                                # staff._meta.verbose_name, staff)
            return redirect(Staff.get_list_url())
        else:
            logging.warning("Staff Form: {}".format(json.dumps(staff_form.errors)))
            messages.warning(request, "Errrorr", "Error")
    else:
        staff_form = form_class(prefix='staff', instance=item, request=request)
    return render(request, template_name, {'staff_form':staff_form, 'staff': staff_list})

def staff_update(request, pk):
    """
    Edits an Staff instance
    """
    return staff_create(request, get_object_or_404(Staff, pk=pk))

def staff_delete(request, pk):
    """
    Deletes an Staff instance
    """
    item = get_object_or_404(Staff, pk=pk)
    # msg = DELETE_SUCCESS.format(item._meta.verbose_name, item)
    item.delete()

    # if request.is_ajax():
    #     return JsonResponse({"msg": msg, "type": TYPE_SUCCESS}, safe=True)
    # else:
    #     messages.warning(request, msg, TITLE_SUCCESS)
    return redirect(Staff.get_list_url())

def staff_detail(request, pk):
    """
    Returns an Staff instance
    """
    instance = get_object_or_404(Staff, pk=pk)
    return render(request, 'department/staff-detail.html', context={'instance':instance})

def staff_list(request, page=1):
    """
    Lists all staffs
    """
    staffs = Staff.objects.filter(enabled=True)
    return render(request, 'department/staff-list.html', context ={'staffs':staffs, 'page':page})