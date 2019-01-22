# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Plantilla
from .forms import PlantillaForm
from django.template import loader
from plantillas.models import Plantilla
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import (
    UpdateView,
    DeleteView,
    CreateView
)
# Create your views here.
def PlantillaNueva(request):
    if request.method == 'POST':
        form = PlantillaForm(request.POST, request.FILES)
        if form.is_valid():
            plantilla = form.save()
            plantilla.save()
            return HttpResponseRedirect('/plantillas')
    else:
        form = PlantillaForm()
    template = loader.get_template('plantillas/new_plantilla.html')
    context = {
        'form': form
    }
    if request.user.is_authenticated():
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('productos:producto_list')


class ListaPlantillaDestacada(ListView):
    template_name = "plantillas/lista-destacado.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Plantilla.objects.all().destacado()

class DetallePlantillaDestacada(DetailView):
    queryset = Plantilla.objects.all().destacado()
    template_name = "plantillas/detalle-destacado.html"

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Plantilla.objects.destacado()



class ListaPlantilla(ListView):
    template_name = "plantillas/lista.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ListaPlantilla,self).get_context_data(*args,**kwargs)
    #     print(context)
    #     return context
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Plantilla.objects.all()

def lista_plantilla(request):
    queryset = Plantilla.objects.all().order_by('nombre')
    context = {
        'qs':queryset
    }
    return render(request, "plantillas/lista.html", context)


class DetallePlantillaMarcado(DetailView):
    queryset = Plantilla.objects.all()
    template_name = "plantillas/detalle.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        marcado = self.kwargs.get('marcado')
        # instancia = get_object_or_404(Plantilla, marcado=marcado, activo=True)
        try:
            instancia = Plantilla.objects.get(marcado=marcado, activo=True)
        except Plantilla.DoesNotExist:
            raise Http404("No se encuentra...")
        except Plantilla.MultipleObjectsReturned:
            qs = Plantilla.objects.filter(marcado=marcado, activo=True)
            instancia = qs.first()
        except:
            raise Http404("¡Uhhmm")
        return instancia


class DetallePlantilla(DetailView):
    # queryset = Plantilla.objects.all()
    template_name = "plantillas/detalle.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DetallePlantilla,self).get_context_data(*args,**kwargs)
        print(context)
        # context = ['abc'] = 123
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instancia = Plantilla.objects.get_by_id(pk)
        if instancia is None:
            raise Http404("¡La Plantilla que buscas no existe!")
        return instancia

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return queryset = Plantilla.objects.filter(pk=pk)


def detalle_plantilla(request, pk=None, *args, **kwargs):
    instancia = Plantilla.objects.get(pk=pk, destacado=True)
    # instancia = get_object_or_404(Plantilla, pk=pk, destacado=True)
    # try:
    #     instancia = Plantilla.objects.get(pk=pk)
    # except Plantilla.DoesNotExist:
    #     print("No hay Plantillas aqui.")
    #     raise Http404("¡El Plantilla que buscas no existe!")
    # except:
    #     print("¿Huh?")
    instancia = Plantilla.objects.get_by_id(pk)
    if instancia is None:
        raise Http404("¡La Plantilla que buscas no existe!")
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
    return render(request, "plantillas/detalle.html", context)

class PlantillaUpdate(UpdateView):
    model = Plantilla
    success_url = reverse_lazy('plantillas:lista')
    fields = ['nombre', 'marcado','descripcion','imagen', 'categoria']
class PlantillaDelete(DeleteView):
    model = Plantilla
    success_url = reverse_lazy('plantillas:lista')
    fields = ['nombre', 'marcado','descripcion','imagen', 'categoria']
