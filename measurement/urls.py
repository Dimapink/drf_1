from django.urls import path

from measurement.views import SensorAPIView, SensorAPIUpdate, MeasurementAPIView, SensorDetailedAPIView

urlpatterns = [
    path("v1/sensors", SensorAPIView.as_view()),
    path("v1/sensors/<int:pk>", SensorAPIUpdate.as_view()),
    path("v1/sensor/<int:pk>", SensorDetailedAPIView.as_view()),
    path("v1/measurements", MeasurementAPIView.as_view())
]
