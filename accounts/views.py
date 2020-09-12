from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages


def logout(request):
    auth.logout(request)
    return redirect("/")


def login(request):
   
        return render(request, "login.html")


def register(request):
    
      return render(request, "register.html")
