# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Desarrollador
from .forms import DesarrolladorForm
from desarrolladores.models import Desarrollador
from django.template import loader
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import (
    UpdateView,
    DeleteView
)
# Create your views here.

class ListaDesarrolladorDestacada(ListView):
    template_name = "desarrollador/lista-destacado.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Desarrollador.objects.all().destacado()

class DetalleDesarrolladorDestacada(DetailView):
    queryset = Desarrollador.objects.all().destacado()
    template_name = "desarrollador/detalle-destacado.html"

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Desarrollador.objects.destacado()



class ListaDesarrollador(ListView):
    template_name = "desarrolladores/lista.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ListaDesarrollador,self).get_context_data(*args,**kwargs)
    #     print(context)
    #     return context
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Desarrollador.objects.all()

def lista_desarrollador(request):
    queryset = Desarrollador.objects.all('nombre')
    context = {
        'qs':queryset
    }
    return render(request, "desarrolladores/lista.html", context)


class DetalleDesarrolladorMarcado(DetailView):
    queryset = Desarrollador.objects.all()
    template_name = "desarrolladores/detalle.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        marcado = self.kwargs.get('marcado')
        # instancia = get_object_or_404(Desarrollador, marcado=marcado, activo=True)
        try:
            instancia = Desarrollador.objects.get(marcado=marcado, activo=True)
        except Desarrollador.DoesNotExist:
            raise Http404("No se encuentra...")
        except Desarrollador.MultipleObjectsReturned:
            qs = Desarrollador.objects.filter(marcado=marcado, activo=True)
            instancia = qs.first()
        except:
            raise Http404("¡Uhhmm")
        return instancia


class DetalleDesarrollador(DetailView):
    # queryset = Desarrollador.objects.all()
    template_name = "desarrolladores/detalle.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DetalleDesarrollador,self).get_context_data(*args,**kwargs)
        print(context)
        # context = ['abc'] = 123
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instancia = Desarrollador.objects.get_by_id(pk)
        if instancia is None:
            raise Http404("¡El Desarrollador que buscas no existe!")
        return instancia

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return queryset = Desarrollador.objects.filter(pk=pk)


def detalle_desarrollador(request, pk=None, *args, **kwargs):
    instancia = Desarrollador.objects.get(pk=pk, destacado=True)
    # instancia = get_object_or_404(Desarrollador, pk=pk, destacado=True)
    # try:
    #     instancia = Desarrollador.objects.get(pk=pk)
    # except Desarrollador.DoesNotExist:
    #     print("No hay Desarrolladores aqui.")
    #     raise Http404("¡El Plantilla que buscas no existe!")
    # except:
    #     print("¿Huh?")
    instancia = Desarrollador.objects.get_by_id(pk)
    if instancia is None:
        raise Http404("¡El Desarrollador que buscas no existe!")
    # print(instancia)
    # qs = Plantilla.objects.filter(id=pk)
    # # print(qs)
    # if qs.exists() and qs.count() == 1: # Longitud del qs
    #     instancia = qs.first()
    # else:
    #     raise Http404("¡La Plantilla que buscas no existe!")
    context = {
        'object':instancia
    }
    return render(request, "desarrolladores/detalle.html", context)

class DesarrolladoresUpdate(UpdateView):
    model = Desarrollador
    success_url = reverse_lazy('desarrolladores:lista')
    fields = ['nombre', 'marcado','cumpleanos','imagen', 'estudios','cv','correo']

class DesarrolladoresDelete(DeleteView):
    model = Desarrollador
    success_url = reverse_lazy('desarrolladores:lista')
    fields = ['nombre', 'marcado','cumpleanos','imagen', 'estudios','cv','correo']

def DesarrolladorNuevo(request):
    if request.method == 'POST':
        form = DesarrolladorForm(request.POST, request.FILES)
        if form.is_valid():
            desarrollador = form.save()
            desarrollador.save()
            return HttpResponseRedirect('/desarrolladores')
    else:
        form = DesarrolladorForm()
    template = loader.get_template('desarrolladores/desarrollador_nuevo.html')
    context = {
        'form': form
    }
    if request.user.is_authenticated():
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('desarrolladores:lista')
