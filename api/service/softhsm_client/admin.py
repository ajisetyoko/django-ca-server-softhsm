from django.contrib import admin

# Register your models here.

from .models import Key
from .forms import KeyForm


class KeyAdminSite(admin.ModelAdmin):
    """
    """

    form = KeyForm


admin.site.register(Key, KeyAdminSite)
