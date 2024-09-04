from rest_framework.generics import (
    ListCreateAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveAPIView)
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


class SensorAPIView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorAPIUpdate(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetailedAPIView(RetrieveAPIView):
    serializer_class = SensorDetailSerializer
    def get_queryset(self):
        queryset = Sensor.objects.filter(pk=self.kwargs["pk"])
        return queryset


class MeasurementAPIView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


