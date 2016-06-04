from django.db import models


class Report(models.Model):
    lat = models.CharField(max_length=200)
    lon = models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    contact=models.CharField(max_length=200)
    urgency=models.CharField(max_length=200)


