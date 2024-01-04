from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUesrAdmin

from core import models

# Register your models here.

# admin.site.register(models.CoreModelTest)


@admin.register(models.User)
class UserAdmin(BaseUesrAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "email",
                    "first_name",
                    "last_name",
                ),
            },
        ),
    )
