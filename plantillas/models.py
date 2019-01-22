# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import random
import os
from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from django.urls import reverse


# Create your models here.
def get_filename_ext(filepath):
    nombre_base = os.path.basename(filepath)
    nombre, ext = os.path.splitext(nombre_base)
    return nombre, ext


def upload_image_path(instancia, nombrearchivo):
    # print(instancia)
    # print(nombrearchivo)
    nuevo_nombrearchivo = random.randint(1,3910209312)
    nombre, ext = get_filename_ext(nombrearchivo)
    nombrearchivo_final = '{nuevo_nombrearchivo}{ext}'.format(nuevo_nombrearchivo=nuevo_nombrearchivo,ext=ext)
    return "plantillas/{nuevo_nombrearchivo}/{nombrearchivo_final}".format(
            nuevo_nombrearchivo=nuevo_nombrearchivo,
            nombrearchivo_final=nombrearchivo_final
            )

class PlantillaQuerySet(models.query.QuerySet):
    def activo(self):
        return self.filter(activo=True)

    def destacado(self):
        return self.filter(destacado=True, activo=True)

class ManejadorPlantilla(models.Manager):
    def get_queryset(self):
        return PlantillaQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().activo()

    def destacado(self): # Plantilla.objects.destacado()
        return self.get_queryset().destacado()

    def get_by_id(self,id):
        qs = self.get_queryset().filter(id=id) # Plantilla.objects == self.get_queryset()
        if qs.count()==1:
            return qs.first()
        return None


class Plantilla(models.Model):
    nombre      = models.CharField(max_length=120)
    marcado     = models.SlugField(blank=True, unique=True)
    descripcion = models.TextField()
    imagen      = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    destacado   = models.BooleanField(default=True)
    activo      = models.BooleanField(default=True)
    categoria   = models.CharField(max_length=120,default='Paginas Web')
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = ManejadorPlantilla()
    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        # return "/plantilla/{marcado}/".format(marcado=self.marcado)
        return reverse("plantillas:detalle", kwargs={"marcado": self.marcado})


def plantilla_pre_guardado_recividor(sender, instance, *arg, **kwargs):
    if not instance.marcado:
        instance.marcado = unique_slug_generator(instance)

pre_save.connect(plantilla_pre_guardado_recividor, sender=Plantilla)
