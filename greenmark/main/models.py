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

PROBABILITY_CHOICES = (
    ('High','High'),
    ('Medium','Medium'),
    ('Low','Low')
)

IF_OCCURS_CHOICES = (
    ('Major','Major'),
    ('Medium','Medium'),
    ('Minor','Minor')
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comp_oblig_name = models.CharField(max_length=50)
    comp_oblig_description = models.TextField()
    env_comm_option = models.CharField(max_length=50, choices=ENVIRON_COMM_CHOICES)
    env_comm_description = models.TextField()

    def __str__(self):
        pass 

class AspImpact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_1 = models.CharField(max_length=50, blank=True)
    aspect_1 = models.CharField(max_length=50, blank=True)
    impact_1 = models.CharField(max_length=50, choices=IMPACTS_CHOICES, blank=True)
    activity_2 = models.CharField(max_length=50, blank=True)
    aspect_2 = models.CharField(max_length=50, blank=True)
    impact_2 = models.CharField(max_length=50, choices=IMPACTS_CHOICES, blank=True)
    activity_3 = models.CharField(max_length=50, blank=True)
    aspect_3 = models.CharField(max_length=50, blank=True)
    impact_3 = models.CharField(max_length=50, choices=IMPACTS_CHOICES, blank=True)
    activity_4 = models.CharField(max_length=50, blank=True)
    aspect_4 = models.CharField(max_length=50, blank=True)
    impact_4 = models.CharField(max_length=50, choices=IMPACTS_CHOICES, blank=True)
    activity_5 = models.CharField(max_length=50, blank=True)
    aspect_5 = models.CharField(max_length=50, blank=True)
    impact_5 = models.CharField(max_length=50, choices=IMPACTS_CHOICES, blank=True)
    activity_6 = models.CharField(max_length=50, blank=True)
    aspect_6 = models.CharField(max_length=50, blank=True)
    impact_6 = models.CharField(max_length=50, choices=IMPACTS_CHOICES, blank=True)
    activity_7 = models.CharField(max_length=50, blank=True)
    aspect_7 = models.CharField(max_length=50, blank=True)
    impact_7 = models.CharField(max_length=50, choices=IMPACTS_CHOICES, blank=True)
    activity_8 = models.CharField(max_length=50, blank=True)
    aspect_8 = models.CharField(max_length=50, blank=True)
    impact_8 = models.CharField(max_length=50, choices=IMPACTS_CHOICES, blank=True)
    activity_9 = models.CharField(max_length=50, blank=True)
    aspect_9 = models.CharField(max_length=50, blank=True)
    impact_9 = models.CharField(max_length=50, choices=IMPACTS_CHOICES, blank=True)
    activity_10 = models.CharField(max_length=50, blank=True)
    aspect_10 = models.CharField(max_length=50, blank=True)
    impact_10 = models.CharField(max_length=50, choices=IMPACTS_CHOICES, blank=True)

    def __str__(self):
        pass 

class EnvThreats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    threat = models.CharField(max_length=50)
    impact = models.CharField(max_length=20, choices=IMPACTS_CHOICES)
    probability = models.CharField(max_length=20, choices=PROBABILITY_CHOICES)
    if_occurs = models.CharField(max_length=20, choices=IF_OCCURS_CHOICES)

    def __str__(self):
        pass 

class Trainers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trainer_name = models.CharField(max_length=50)
    trainer_email = models.CharField(max_length=50)
    trainee_name = models.CharField(max_length=50)
    trainee_email = models.CharField(max_length=50)

    def __str__(self):
        return 
