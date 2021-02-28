from django.shortcuts import render
from django.http import HttpResponse
from .models import vehmgt
from django.utils import timezone
from datetime import *

def index(request):
    return render(request, "index.html")


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def employees(request):
    return render(request, "employees.html")


def achievements(request):
    return render(request, "achievements.html")


def contact(request):
    return render(request, "contact.html")


def biodata(request):

    if request.method == 'POST':
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')

        t = vehmgt.objects.raw(
            'select token,veh,time,location from vehlog where time between "'+date1+'" and "'+date2+'" ')
        return render(request, "biodata.html", {"dests": t})

    # elif request.method == 'POST':
    #     vehicle = request.POST.get('veh')

    #     v = vehmgt.objects.raw(
    #             'select token,veh,time,location from vehlog where veh = "vehicle"')

    #     return render(request, "biodata.html", {"dests": v})


    else:
        dest = vehmgt.objects.all()
        return render(request, "biodata.html", {"dests": dest})


def insert(request):
    return render(request, "insert.html")



