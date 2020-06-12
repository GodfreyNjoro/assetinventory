from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from core.models import CoreModel as CM
from .managers import UserManager

class User(PermissionsMixin, CM, AbstractBaseUser):
    VENDOR = "Vendor"
    CLIENT = "Client"
    Courier = "Courier"

    ROLES = {
            (VENDOR,'Vendor'),
            (CLIENT, 'Client'),
            (Courier, 'Courier')
            }

    username = models.CharField(
            _('username'),
            unique=True,
            max_length=20,
            help_text=_('Required. 20 characters or fewer. Letters, digits and @/./+/-/_ only.'),
            error_messages={'unique': _("A user with that username already exists."),}
        )

    email = models.EmailField(
            _('email address'),
            unique=True,
            max_length=128,
            help_text=_('Required valid email'),
            error_messages={'unique': _("A user with that email already exists."), },
            null=True,
            blank=True,
            default=None
        )
    first_name = models.CharField(verbose_name=_("first name"), max_length=30, blank=True, null=True)
    last_name = models.CharField(verbose_name=_("last name"), max_length=30, blank=True, null=True)
    phone = models.CharField(
            _('phone number'),
            unique=True,
            max_length=9,
            help_text=_('Require valid phone number'),
            blank=True,
            null=True,
            default=None
        )
    role = models.CharField(max_length=12, choices=ROLES, default=CLIENT)
    is_staff = models.BooleanField(
        _("staff status"), default=False, help_text=_("Designates whether the user can log into this admin site.")
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. " "Unselect this instead of deleting accounts."
        ),
    )
    verified = models.BooleanField(_("is verified"), default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    #EMAIL_FIELD = ''
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        ordering = ("username", )



