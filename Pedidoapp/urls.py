from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url
from .import views
from django.contrib.auth.views import login_required

from Pedidoapp.views import home, Cant_ingresar, add,  Aprobado, ListAll, ListEspeci, Cant_update

admin.autodiscover()

urlpatterns = [

url(r'^home/$', login_required(home), name="home"),

url(r'^lista_super/(?P<id_especialidad>\d+)/$', login_required(ListAll), name='lita_todo'),
url(r'^lista_active/(?P<id_especialidad>\d+)/$', login_required(ListEspeci), name='lita_active'),
url(r'^confirmar/(?P<id_pedido>\d+)', login_required(Aprobado), name='aprobar_pedido'),
#url(r'^ingresar/$', login_required(add), name="ingresar_cant"),
url(r'^ingresar/(?P<id_pedido>\d+)//(?P<id_especialidad>\d+)/$', Cant_ingresar, name="cant_ingresar"),
url(r'^modificar/(?P<id_pedido>\d+)//(?P<id_especialidad>\d+)/$', Cant_update, name="cant_update"),


]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#(?P<cod_experto>\d+)