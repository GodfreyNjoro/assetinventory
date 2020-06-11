from django.contrib.auth.models import BaseUserManager
from core.models import CoreQuerySet

class UserManager(BaseUserManager):
    def get_queryset(self):
        return CoreQuerySet(self.model, using=self._db)

    def create_user(self, username, email=None, password=None, phone=None,  **extra_fields):
        if not username:
            raise ValueError("Username must be set")

        user = self.model(username=username, email=email, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

