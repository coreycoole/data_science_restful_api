from rest_framework import viewsets
from .models import InputData
from .serializers import InputDataSerializer

class InputDataViewset(viewsets.ModelViewSet):
    queryset = InputData.objects.all()
    serializer_class = InputDataSerializer


