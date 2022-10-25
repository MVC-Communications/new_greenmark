from random import choices
from django.db import models
from django.contrib.auth.models import User


ENVIRON_COMM_CHOICES = (
    ('suggestion','suggestion'),
    ('positive feedback','positive feedback'),
    ('complaints','complaints'),
    ('requests', 'requests')
)

IMPACTS_CHOICES = (
    ('Land','Land'),
    ('Air','Air'),
    ('Water','Water')
)

class BussInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year_of_aggrement = models.DateField()
    buss_name = models.CharField(max_length=50)
    # buss_logo = models.ImageField(upload_to='media/BusinessLogos')
    phone = models.CharField(max_length=15)
    website = models.CharField(max_length=50)
    location1 = models.CharField(max_length=70)
    location2 = models.CharField(max_length=70, blank=True)
    location3 = models.CharField(max_length=70, blank=True)
    location4 = models.CharField(max_length=70, blank=True)
    keydecider_name = models.CharField(max_length=30)
    keydecider_title = models.CharField(max_length=30)
    keydecider_email = models.CharField(max_length=30)
    keydecider_signature = models.CharField(max_length=30)
    envmanager_name = models.CharField(max_length=30)
    envmanager_title = models.CharField(max_length=30)
    envmanager_email = models.CharField(max_length=30)
    envmanager_signature = models.CharField(max_length=30)
    otherresp_person_name = models.CharField(max_length=30, blank=True)
    otherresp_person_title = models.CharField(max_length=30, blank=True)
    otherresp_person_email = models.CharField(max_length=30, blank=True)
    otherresp_person_signature = models.CharField(max_length=30, blank=True)
    

    def __str__(self):
        pass 

class EnvCompOblig(models.Model):
    document = models.ForeignKey(BussInfo, on_delete=models.CASCADE)
    comp_oblig_name = models.CharField(max_length=50)
    comp_oblig_description = models.TextField()
    env_comm_option = models.CharField(max_length=50, choices=ENVIRON_COMM_CHOICES)
    env_comm_description = models.TextField()

    def __str__(self):
        pass 

class AspImpact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_1 = models.CharField(max_length=50)
    aspect_1 = models.CharField(max_length=50)
    impact_1 = models.CharField(max_length=50)
    activity_2 = models.CharField(max_length=50)
    aspect_2 = models.CharField(max_length=50)
    impact_2 = models.CharField(max_length=50)
    activity_3 = models.CharField(max_length=50)
    aspect_3 = models.CharField(max_length=50)
    impact_3 = models.CharField(max_length=50)
    activity_4 = models.CharField(max_length=50)
    aspect_4 = models.CharField(max_length=50)
    impact_4 = models.CharField(max_length=50)

    def __str__(self):
        pass 