from django.conf.urls import url
from .views import (
        ListaDesarrollador,
        DetalleDesarrolladorMarcado,
        DesarrolladorNuevo
        )



urlpatterns = [
    url(r'^$', ListaDesarrollador.as_view(),name='lista'),
    url(r'^NuevoDesarrollador/$', DesarrolladorNuevo,name='nuevo'),
    url(r'^(?P<marcado>[\w-]+)/$', DetalleDesarrolladorMarcado.as_view(), name='detalle'),
]
