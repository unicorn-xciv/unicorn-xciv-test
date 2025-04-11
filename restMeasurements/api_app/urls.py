from django.urls import path
from .views import MeasurementItemViews


urlpatterns = [
    path('measurement-items/', MeasurementItemViews.as_view()),
    path('measurement-items/<int:id>', MeasurementItemViews.as_view())
]
