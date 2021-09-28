from rest_framework import viewsets, views
from rest_framework.response import Response
from .models import InputData
from .serializers import InputDataSerializer

class InputDataViewset(viewsets.ModelViewSet):
    queryset = InputData.objects.all()
    serializer_class = InputDataSerializer


class BasicDataTestView(views.APIView):

    @staticmethod
    def get(request):
        return Response({"status": "successful", "payload": ["Hello World"]})

    @staticmethod
    def post(input_data):
        """find out how to post data to ML algo"""
        return None



