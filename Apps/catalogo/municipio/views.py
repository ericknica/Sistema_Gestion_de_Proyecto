from rest_framework import viewsets
from .models import Municipio
from .serializers import MunicipioSerializer

class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer