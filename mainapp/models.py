from django.db import models
from datetime import *

class vehmgt(models.Model):
    token = models.IntegerField(primary_key=True)
    veh = models.CharField(max_length=7)
    time = models.DateTimeField(null=True)
    location = models.CharField(max_length=100)
   
    class Meta:
        db_table="vehlog"
