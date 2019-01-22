from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import (
        ListaPlantilla,
        DetallePlantillaMarcado,
        PlantillaNueva,
        PlantillaUpdate,
        PlantillaDelete

        )



urlpatterns = [
    url(r'^$', ListaPlantilla.as_view(),name='lista'),
    url(r'^Nueva/',PlantillaNueva,name="nueva"),
    url(r'^(?P<marcado>[\w-]+)/$', DetallePlantillaMarcado.as_view(), name='detalle'),
    url(r'^Actualizar/(?P<pk>\d+)/$', PlantillaUpdate.as_view(), name='actualizar'),
    url(r'^Eliminar/(?P<pk>\d+)/$', PlantillaDelete.as_view(), name='eliminar'),
]
