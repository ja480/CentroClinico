from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('account/', include('accounts.urls', namespace='accounts')),
    path('patients/', include('patients.urls', namespace="patients")),
    path('doctors/', include('doctors.urls', namespace="doctors")),
]
