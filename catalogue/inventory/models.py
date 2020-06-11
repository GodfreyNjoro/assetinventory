from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import CoreModel as CM

UserModel = get_user_model()
SELECT_EMPTY = ('', '------')

class Asset(CM):
    """
    This model holds the data of an asset ie. Laptop etc..
    """

    tag_id = models.CharField(_('Asset Tag ID'), max_length=254, unique=True)
    description = models.TextField(_('Asset Description'), max_length=140, help_text=_('Description of the asset'))
    purchase_date = models.DateTimeField(_('Purchase Date'), help_text=_("Date asset was purchased"))
    cost = models.DecimalField(_('Cost'), default=0, max_digits=10, decimal_places=2, help_text=_("Cost of the asset"))
    purchased_from = models.CharField(_('Purchased From'), max_length=100, help_text=_('Vendor/Supplier name'))
    brand = models.CharField(_('Brand'), max_length=100, null=True, blank=True, help_text=_('Manufacturer of the asset'))
    model = models.CharField(_('Model'), max_length=100, null=True, blank=True, help_text=_('Model name of the asset'))
    serial_no = models.CharField(_('Serial No'), max_length=100, null=True, blank=True, unique=True, help_text=_('Manufacturers serial No.'))
    photo = models.ImageField(_('Asset Photo'), upload_to='images', blank=True, null=True, default=None)
    category = models.ForeignKey('AssetCategory', on_delete=models.CASCADE, related_name="asset")
    enabled = models.BooleanField(_('enabled'), default=True)

    def __str__(self):
        return self.tag_id

    class Meta:
        ordering = ('created', 'purchase_date', )

    @classmethod
    def get_add_url(cls):
        return reverse('inventory:asset-add')

    @classmethod
    def get_list_url(cls):
        return reverse('inventory:asset-list')

    def get_absolute_url(self):
        return reverse('inventory:asset-detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('inventory:asset-edit', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('inventory:asset-delete', kwargs={'pk': self.pk})


class AssetCategory(CM):
    """
    This is a the category type of an asset
    """
    name = models.CharField(_('Name'), max_length=100, unique=True, error_messages={'unique': _("A category with that name already exists ;-)")})
    enabled = models.BooleanField(_('enabled'), default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created', 'name', )

    @classmethod
    def get_add_url(cls):
        return reverse('inventory:category-add')

    @classmethod
    def get_list_url(cls):
        return reverse('inventory:category-list')

    def get_absolute_url(self):
        return reverse('inventory:category-detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('inventory:category-edit', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('inventory:category-delete', kwargs={'pk': self.pk})
