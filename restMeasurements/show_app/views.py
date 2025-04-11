from django.shortcuts import render
from django.utils import timezone


# Create your views here.

from django.db.models import Count,F,Sum,Avg
from django.db.models.functions import ExtractYear,ExtractMonth
from django.http import JsonResponse
from api_app.models import MeasurementItem
from .utils import (
    colorDanger, colorPalette,
    colorPrimary,colorSuccess,
    generate_color_palette)
# Create your views here.

def display_charts(request):
    return render(request, 'charts.html', {})


def displayHumidity(request):

    local_tz = timezone.get_current_timezone() 

    temp_hum = MeasurementItem.objects.all()
    humidityList = MeasurementItem.objects.values_list('humidity')
    timestampList = MeasurementItem.objects.values_list('timestamp')

    numElements = len(humidityList)

    hList = []
    tsList = []

    for id in range(numElements):
        hList.append(float(humidityList[id][0]))

    for id in range(numElements):

        timestampFromDb = timestampList[id][0]
        datetimeLocal = timestampFromDb.astimezone(local_tz)
        timestamp = str(datetimeLocal)

        timestamp = timestamp.split('.')[0]
        tsList.append(timestamp)

    return JsonResponse({
        'title' : f'Humidity',
        'data': {
            'labels': tsList,
            'datasets': [{
                'label': 'Humidity (%)',
                'backgroundColor': generate_color_palette(1),
                'borderColor': generate_color_palette(numElements),
                'data': hList,
            }]
        },
    }    )


def displayTemperatures(request):

    local_tz = timezone.get_current_timezone()

    temp_hum = MeasurementItem.objects.all()
    temperaturesList = MeasurementItem.objects.values_list('temperature')

    timestampList = MeasurementItem.objects.values_list('timestamp')

    numElements = len(temperaturesList)

    tList = []

    tsList = []

    for id in range(numElements):
        tList.append(float(temperaturesList[id][0]))



    for id in range(numElements):
        timestampFromDb = timestampList[id][0]
        datetimeLocal = timestampFromDb.astimezone(local_tz)
        timestamp = str(datetimeLocal)
        
        timestamp = timestamp.split('.')[0]
        tsList.append(timestamp)



    return JsonResponse({
        'title' : f'Temperature',
        'data': {
            'labels': tsList,
            'datasets': [{
                'label': 'Temperature (°C)',
                'backgroundColor': colorPalette[2],
                'borderColor': generate_color_palette(numElements),
                'data': tList,
            }]
        },
    }    )


def displayBrightness(request):

    local_tz = timezone.get_current_timezone()

    temp_hum = MeasurementItem.objects.all()
    brightnessList = MeasurementItem.objects.values_list('brightness')
    timestampList = MeasurementItem.objects.values_list('timestamp')

    numElements = len(brightnessList)

    bList = []
    tsList = []

    for id in range(numElements):
        bList.append(float(brightnessList[id][0]))

    for id in range(numElements):
        timestampFromDb = timestampList[id][0]
        datetimeLocal = timestampFromDb.astimezone(local_tz)
        timestamp = str(datetimeLocal)

        timestamp = timestamp.split('.')[0]
        tsList.append(timestamp)

    return JsonResponse({
        'title' : f'Brightness',
        'data': {
            'labels': tsList,
            'datasets': [{
                'label': 'Brightness (lx)',
                'backgroundColor': colorPalette[3],
                'borderColor': generate_color_palette(numElements),
                'data': bList,
            }]
        },
    }    )


def displayPressure(request):

    local_tz = timezone.get_current_timezone()

    temp_hum = MeasurementItem.objects.all()
    pressuresList = MeasurementItem.objects.values_list('atmosphericPressure')
    timestampList = MeasurementItem.objects.values_list('timestamp')

    numElements = len(pressuresList)

    pList = []
    tsList = []

    for id in range(numElements):
        pList.append(float(pressuresList[id][0]))

    for id in range(numElements):
        timestampFromDb = timestampList[id][0]
        datetimeLocal = timestampFromDb.astimezone(local_tz)
        timestamp = str(datetimeLocal)

        timestamp = timestamp.split('.')[0]
        tsList.append(timestamp)

    return JsonResponse({
        'title' : f'Atmospheric pressure',
        'data': {
            'labels': tsList,
            'datasets': [{
                'label': 'Atmospheric pressure (hPa)',
                'backgroundColor': colorPalette[6],
                'borderColor': generate_color_palette(numElements),
                'data': pList,
            }]
        },
    }    )

