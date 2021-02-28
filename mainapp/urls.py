from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.home, name='home'),
    path('about.html', views.about, name='about'),
    path('employees.html', views.employees, name='employees'),
    path('achievements.html', views.achievements, name='achievements'),
    path('contact.html', views.contact, name='contact'),
    path('biodata.html', views.biodata, name='biodata'),
    path('insert.html', views.insert, name='insert'),
    
    
]
