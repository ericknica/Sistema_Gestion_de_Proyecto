from rest_framework.routers import DefaultRouter
from .views import DepartamentoViewSet

router = DefaultRouter()
router.register('departamentos', DepartamentoViewSet, basename='departamento')

urlpatterns = router.urls
