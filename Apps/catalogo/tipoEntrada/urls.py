from rest_framework.routers import DefaultRouter
from .views import TipoEntradaViewSet

router = DefaultRouter()
router.register(r'tipos-entrada', TipoEntradaViewSet)

urlpatterns = router.urls