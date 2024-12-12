from rest_framework.viewsets import ModelViewSet
from .models import Departamento
from .serializers import DepartamentoSerializer

class DepartamentoViewSet(ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
