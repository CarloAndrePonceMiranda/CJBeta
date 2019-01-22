# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Plantilla
# Register your models here.
class PlantillaAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    class Meta:
        model = Plantilla

admin.site.register(Plantilla, PlantillaAdmin)
