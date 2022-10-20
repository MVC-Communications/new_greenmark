from random import choices
from django.db import models


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

class AgreementDoc(models.Model):
    # doc_id = models.BigAutoField(primary_key=True)
    year_made = models.DateField()

    def __str__(self):
        pass 

class BussInfo(models.Model):
    # doc_id = models.ForeignKey(AgreementDoc, on_delete=models.CASCADE)
    # buss_id = models.BigAutoField(primary_key=True)
    buss_name = models.CharField(max_length=50)
    # buss_logo = models.ImageField(upload_to='media/BusinessLogos')
    phone = models.CharField(max_length=15)
    website = models.CharField(max_length=50)
    location1 = models.CharField(max_length=70)
    location2 = models.CharField(max_length=70, blank=True)
    location3 = models.CharField(max_length=70, blank=True)
    location4 = models.CharField(max_length=70, blank=True)

    def __str__(self):
        pass 

class KeyDecisionMaker(models.Model):
    # doc_id = models.ForeignKey(AgreementDoc, on_delete=models.CASCADE)
    # buss_id = models.ForeignKey(BussInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    signature = models.CharField(max_length=30)

class EnvironManager(models.Model):
    # doc_id = models.ForeignKey(AgreementDoc, on_delete=models.CASCADE)
    # buss_id = models.ForeignKey(BussInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    signature = models.CharField(max_length=30)

class OtherResponsiblePerson(models.Model):
    # doc_id = models.ForeignKey(AgreementDoc, on_delete=models.CASCADE)
    # buss_id = models.ForeignKey(BussInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    signature = models.CharField(max_length=30)

class EnvCompOblig(models.Model):
    # doc_id = models.ForeignKey(AgreementDoc, on_delete=models.CASCADE)
    # buss_id = models.ForeignKey(BussInfo, on_delete=models.CASCADE)
    agreement_name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        pass 

class EnvComm(models.Model):
    # doc_id = models.ForeignKey(AgreementDoc, on_delete=models.CASCADE)
    # buss_id = models.ForeignKey(BussInfo, on_delete=models.CASCADE)
    comm_option = models.CharField(max_length=50, choices=ENVIRON_COMM_CHOICES)
    description = models.TextField()

    def __str__(self):
        pass 
