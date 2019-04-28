from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from apps.usuario.views import RegistroUsuario
urlpatterns = [
    url(r'^registrar', login_required(RegistroUsuario.as_view()), name="registrar"),
    # url(r'^api',login_required(UserAPI.as_view()), name='api')

]
