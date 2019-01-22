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
    return "desarrolladores/{nuevo_nombrearchivo}/{nombrearchivo_final}".format(
            nuevo_nombrearchivo=nuevo_nombrearchivo,
            nombrearchivo_final=nombrearchivo_final
            )
#C.V


def upload_cv_path(instancia, nombrearchivo):
    # print(instancia)
    # print(nombrearchivo)
    nuevo_nombrearchivo = random.randint(1,3910209312)
    nombre, ext = get_filename_ext(nombrearchivo)
    nombrearchivo_final = '{nuevo_nombrearchivo}{ext}'.format(nuevo_nombrearchivo=nuevo_nombrearchivo,ext=ext)
    return "cvs/{nuevo_nombrearchivo}/{nombrearchivo_final}".format(
            nuevo_nombrearchivo=nuevo_nombrearchivo,
            nombrearchivo_final=nombrearchivo_final
            )

class DesarrolladorQuerySet(models.query.QuerySet):
    def activo(self):
        return self.filter(activo=True)

    def destacado(self):
        return self.filter(destacado=True, activo=True)

class ManejadorDesarrollador(models.Manager):
    def get_queryset(self):
        return DesarrolladorQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().activo()

    def destacado(self): # Desarrollador.objects.destacado()
        return self.get_queryset().destacado()

    def get_by_id(self,id):
        qs = self.get_queryset().filter(id=id) # Desarrollador.objects == self.get_queryset()
        if qs.count()==1:
            return qs.first()
        return None


class Desarrollador(models.Model):
    nombre      = models.CharField(max_length=120)
    marcado     = models.SlugField(blank=True, unique=True)
    cumpleanos  = models.DateField()
    imagen      = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    activo      = models.BooleanField(default=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    estudios    = models.CharField(blank=True, max_length=100)
    cv          = models.FileField(upload_to=upload_cv_path, null=True, blank=True)
    correo      = models.EmailField()
    destacado   = models.BooleanField(default=True)


    objects = ManejadorDesarrollador()
    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        # return "/desarrollador/{marcado}/".format(marcado=self.marcado)
        return reverse("desarrolladores:detalle", kwargs={"marcado": self.marcado})


def desarrollador_pre_guardado_recividor(sender, instance, *arg, **kwargs):
    if not instance.marcado:
        instance.marcado = unique_slug_generator(instance)

pre_save.connect(desarrollador_pre_guardado_recividor, sender=Desarrollador)
