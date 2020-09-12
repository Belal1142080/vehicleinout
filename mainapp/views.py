from django.shortcuts import render
from django.http import HttpResponse
from .models import destination


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

    dests = destination.objects.all()
    return render(request, "biodata.html", {'dests': dests})


def insert(request):
    return render(request, "insert.html")
