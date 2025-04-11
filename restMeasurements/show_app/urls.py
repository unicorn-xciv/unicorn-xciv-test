from django.urls import path
from .import views


urlpatterns = [
    path('showall', views.display_charts, name='index'),
    path('temp', views.displayTemperatures,name='displayTemperatures'),
    path('hum', views.displayHumidity,name='displayHumidity'),
    path('bright', views.displayBrightness,name='displayBrightness'),
    path('pressure', views.displayPressure,name='displayPressure'),
]
