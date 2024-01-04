from django.contrib import admin
from . import models


# Register your models here.


@admin.register(models.Blogger)
class BloggerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name"]
    list_select_related = ["user"]
    ordering = ["user__first_name", "user__last_name"]
