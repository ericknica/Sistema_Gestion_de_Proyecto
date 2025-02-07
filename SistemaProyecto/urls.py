"""
URL configuration for SistemaProyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt import views as jwt_views



schema_view = get_schema_view(
    openapi.Info(
        title="Sistema de Gestión de Proyectos",
        default_version='v1',
        description="Documentación de la API para el sistema de gestión de proyectos",
    ),
    public=True,
    permission_classes=(AllowAny,),
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/catalogo/', include('Apps.catalogo.departamento.urls')),
    path('api/seguridad/', include('Apps.seguridad.usuarios.urls')),
    path('proyecto/catalogo/', include('Apps.catalogo.urls')), 
    path('municipio/', include('Apps.catalogo.municipio.urls')),
    path('tipo-entrada/', include('Apps.catalogo.tipoEntrada.urls')),
    path('tipo-salida/', include('Apps.catalogo.tipoSalida.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view()),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view()),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='Documentacion'),
]

