# apps/catalogos/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProyectoViewSet, TareaViewSet


router = DefaultRouter()
router.register(r'proyectos', ProyectoViewSet)
router.register(r'tareas', TareaViewSet)

urlpatterns = router.urls