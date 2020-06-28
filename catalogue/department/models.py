from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from core.models import CoreModel as CM
from location.models import Location, Site
UserModel = get_user_model()

class Department(CM):
    """
    This are individual units of a Company
    designated to work together accomplish a common goal
    """

    name = models.CharField("Department Name", max_length=128, unique=True, error_messages={'unique': _("A department with that name already exists ;-)")})
    enabled = models.BooleanField(_('enabled'), default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('created', 'name', )
    
    @classmethod
    def get_add_url(cls):
        return reverse('department:department-add')

    @classmethod
    def get_list_url(cls):
        return reverse('department:department-list')

    def get_absolute_url(self):
        return reverse('department:department-detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('department:department-edit', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('department:department-delete', kwargs={'pk': self.pk})


class Staff(CM):
    """
    Company staff
    """

    #user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(_("Full Name"), max_length=128, default=None, null=True, blank=True)
    employee_id = models.CharField(_("Employee ID"), max_length=128, default=None, null=True, blank=True)
    title = models.CharField(_("Title"), max_length=128, default=None, null=True, blank=True)
    notes = models.TextField(_('Notes'), max_length=140, blank=True, null=True)
    #site = models.ForeignKey(Site, on_delete=models.CASCADE, default=None, null=True, blank=True, related_name="staff")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=None, null=True, blank=True, related_name="staff")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=None, blank=True, related_name="staff")
    enabled = models.BooleanField(_('enabled'), default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('created', 'name', )

    @classmethod
    def get_add_url(cls):
        return reverse('department:staff-add')

    @classmethod
    def get_list_url(cls):
        return reverse('department:staff-list')

    def get_absolute_url(self):
        return reverse('department:staff-detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('department:staff-edit', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('department:staff-delete', kwargs={'pk': self.pk})

