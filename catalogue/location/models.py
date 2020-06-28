from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from core.models import CoreModel as CM

UserModel = get_user_model()
SELECT_EMPTY = ('', '------')

class Site(CM):
    """
    Holds Company Site information
    """
    name = models.CharField(_('Site Name'), max_length=254, unique=True)
    description = models.TextField(_('Site Description'), max_length=140, help_text=_('Description of the site'))
    address = models.CharField(_('Address'),max_length=254  )
    apt = models.CharField(_('Apt/Suite'), max_length=254, null=True, blank=True, default=None)
    city = models.CharField(_('City'), max_length=32)
    state = models.CharField(_('State'), max_length=32)
    zip = models.CharField(_('Zip'), max_length=10)
    country = models.CharField(_('Country'), max_length=32)
    enabled = models.BooleanField(_('enabled'), default=True)

    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created', 'name', )

    @classmethod
    def get_add_url(cls):
        return reverse('location:site-add')

    @classmethod
    def get_list_url(cls):
        return reverse('location:site-list')

    def get_absolute_url(self):
        return reverse('location:site-detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('location:site-edit', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('location:site-delete', kwargs={'pk': self.pk})

    
class Location(CM):
    """
    Holds Company Location
    """

    site = models.ForeignKey('Site', on_delete=models.CASCADE, related_name='locations')
    name = models.CharField("Location Name", max_length=128, unique=True, error_messages={'unique': _("A location with that name already exists ;-)")})
    enabled = models.BooleanField(_('enabled'), default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('created', 'name', )
    
    @classmethod
    def get_add_url(cls):
        return reverse('location:location-add')

    @classmethod
    def get_list_url(cls):
        return reverse('location:location-list')

    def get_absolute_url(self):
        return reverse('location:location-detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('location:location-edit', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('location:location-delete', kwargs={'pk': self.pk})
