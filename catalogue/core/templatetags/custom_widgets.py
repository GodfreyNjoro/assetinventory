from datetime import date

from django import template
from django.template.defaultfilters import stringfilter
from django.urls import reverse
from django.utils.safestring import mark_safe
from datetime import datetime
from django.template.defaultfilters import timesince
from django.db.models import FieldDoesNotExist


register = template.Library()

def icon_widget(val, label, icon, date=""):
    html = mark_safe(f"""<div class="form-group col-sm-12">
                <label>{label}</label>
                <div class="input-group {date}">
                    <span class="input-group-text input-group-append input-group-addon">
                        {icon}
                    </span>
                    {val}
                </div> 
            </div>""")
    return html


@register.filter("_date_widget")
def _date_widget(val, arg):
    icon = """<i class="simple-icon-calendar float-left"></i>"""
    return icon_widget(val, arg, icon, date="date")


@register.filter("_ksh_widget")
def _ksh_widget(val, arg):
    icon = "Ksh"
    return icon_widget(val, arg, icon)

@register.filter(name="assign_icon")
def assign_icon(obj, default=""):
    if obj:
        return mark_safe("<a href='{}' title='Delete {}' data-toggle='tooltip'><i class='simple-icon-trash text-danger'></i></a>".format(obj.get_assign_url(), obj))
    else:
        return default

@register.filter(name="delete_icon")
def delete_icon(obj, default=""):
    if obj:
        return mark_safe("<a href='{}' title='Delete {}' data-toggle='tooltip'><i class='simple-icon-trash text-danger'></i></a>".format(obj.get_delete_url(), obj))
    else:
        return default

@register.filter(name="edit_icon")
def edit_icon(obj, default=""):
    if obj:
        return mark_safe("<a href='{}' title='Edit {}' data-toggle='tooltip'><i class='simple-icon-note text-primary'></i></a>".format(obj.get_update_url(), obj))
    else:
        return default

