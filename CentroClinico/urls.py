"""CentroClinico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from CentroClinico.views import *
from citas.views import *

# from CentroClinico.views import index, regcita, sobrenosotros, servicios, crearcuenta,adminlogin,Login_admin,MakeAppointments
# from citas.views import ListadoCita, DetallesCita, CrearCita, CitasEliminar, CitasActualizar



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', servicios),
    path('admin_login/',Login_admin,name='login_admin'),
    path('login/',loginpage,name='loginpage'),
    path('logout/',Logout,name='logout'),
    path('index/',index,name='index'),
    path('indexadmin/',indexadmin,name='indexadmin'),
    path('makeappointments/',MakeAppointments,name='makeappointments'),
    # path('makeappointments/',MakeAppointments,name='makeappointments'),
    path('servicios/', servicios),
    path('sobrenosotros/', sobrenosotros),
    path('crearcuenta/', crearcuenta),
    # path('account/', include('django.contrib.auth.urls')),
    path('citas/', ListadoCita.as_view(template_name = 'citas/Citas.html'), name='leer'),
    path('citas/detalle/<int:pk>', DetallesCita.as_view(template_name = 'citas/DetallesCitas.html'), name = 'detalle'),
    path('citas/crear/', CrearCita.as_view(template_name = 'citas/CrearCita.html'), name = 'crear'),
    path('citas/eliminar/<int:pk>', CitasEliminar.as_view(), name = 'eliminar'),
    path('citas/actualizar/<int:pk>', CitasActualizar.as_view(template_name = 'citas/ActualizarCitas.html'), name = 'actualizar'),
]
