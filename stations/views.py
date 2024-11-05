from django.shortcuts import render, redirect
from django.urls import reverse

from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open('data-398-2018-08-30.csv', 'r', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        stations = list(reader)
    
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(stations, 10)
    page_obj = paginator.get_page(page_number)
    
    context = {
        'bus_stations': page_obj.object_list,
        'page': page_obj,
    }
    return render(request, 'stations/index.html', context)
