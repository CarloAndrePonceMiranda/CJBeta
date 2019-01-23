from django.conf.urls import url
from .views import (
        ListaDesarrollador,
        DetalleDesarrolladorMarcado,
        DesarrolladorNuevo,
        DesarrolladoresDelete,
        DesarrolladoresUpdate,
        )



urlpatterns = [
    url(r'^$', ListaDesarrollador.as_view(),name='lista'),
    url(r'^NuevoDesarrollador/$', DesarrolladorNuevo,name='nuevo'),
    url(r'^Actualizar/(?P<pk>\d+)/$', DesarrolladoresUpdate.as_view(), name='actualizar'),
    url(r'^Eliminar/(?P<pk>\d+)/$', DesarrolladoresDelete.as_view(), name='eliminar'),
    url(r'^(?P<marcado>[\w-]+)/$', DetalleDesarrolladorMarcado.as_view(), name='detalle'),
]
