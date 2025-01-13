from django.contrib import admin
from django.urls import path, include

from autenticacion import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crud.urls')),
    path('', include('autenticacion.urls')),
]
