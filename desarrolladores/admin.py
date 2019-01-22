# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Desarrollador
# Register your models here.
class DesarrolladorAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    class Meta:
        model = Desarrollador

admin.site.register(Desarrollador, DesarrolladorAdmin)
