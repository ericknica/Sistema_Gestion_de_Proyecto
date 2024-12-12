from rest_framework.routers import DefaultRouter
from .views import TipoSalidaViewSet

router = DefaultRouter()
router.register(r'tipos-salida', TipoSalidaViewSet)

urlpatterns = router.urls