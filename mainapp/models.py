from django.db import models
from datetime import *


class destination(models.Model):
    token = models.CharField(max_length=100)
    veh = models.CharField(max_length=100)
    time = datetime.now()
    location = models.CharField(max_length=100)
    desc = models.TextField()
