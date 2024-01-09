from pprint import pprint
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.db.models import Q
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


# Create your models here.
class CoreModelTest(models.Model):
    """Model definition for CoreModelTest."""

    # TODO: Define fields here
    title = models.CharField(_("Titel"), max_length=50)

    class Meta:
        """Meta definition for CoreModelTest."""

        verbose_name = "CoreModelTest"
        verbose_name_plural = "CoreModelTests"

    def __str__(self):
        """Unicode representation of CoreModelTest."""
        pass

    def get_title_by_id(pk):
        coreModelObject = CoreModelTest.objects.get(pk=pk)
        return coreModelObject


class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        pprint(self.model.phone)
        return self.get(
            Q(**{self.model.USERNAME_FIELD: username})
            | Q(**{self.model.EMAIL_FIELD: username})
            # | Q(**{self.model.phone: username})
        )


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    objects = CustomUserManager()
