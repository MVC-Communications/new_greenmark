from unicodedata import name
from django.db import models

# year 

class BussInfo(models.Model):
    buss_id = models.BigAutoField(primary_key=True)
    buss_name = models.CharField(max_length=50)
    buss_logo = models.ImageField(upload_to=None)
    phone = models.CharField(max_length=15)
    website = models.CharField(max_length=50)
    location1 = models.CharField(max_length=70)
    location2 = models.CharField(max_length=70, blank=True)
    location3 = models.CharField(max_length=70, blank=True)
    location4 = models.CharField(max_length=70, blank=True)

    def __str__(self):
        return 

    def __unicode__(self):
        return 

class KeyDecisionMaker(models.Model):
    buss_id = models.ForeignKey(BussInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    signature = models.ImageField(upload_to=None)

class EnvironManager(models.Model):
    buss_id = models.ForeignKey(BussInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    signature = models.ImageField(upload_to=None)