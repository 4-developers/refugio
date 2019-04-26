from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from apps.mascota.views import index, listadousuarios, MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', login_required(MascotaCreate.as_view()), name='mascota_crear'),
    url(r'^listar$', login_required(MascotaList.as_view()), name='mascota_listar'),
    url(r'^editar/(?P<pk>\d)$', login_required(MascotaUpdate.as_view()), name='mascota_editar'),
    url(r'^eliminar/(?P<pk>\d)$', login_required(MascotaDelete.as_view()), name='mascota_delete'),
    url(r'^listado', listadousuarios, name='listado')
]
