from dataclasses import field
from pyexpat import model
from django.forms import ModelForm

from .models import *

class BussInfoForm(ModelForm):
    class Meta:
        model = BussInfo
        exclude = ['user']
class EnvCompObligForm(ModelForm):
    class Meta:
        model = EnvCompOblig
        exclude = ['user']

class AspImpactForm(ModelForm):
    class Meta:
        model = AspImpact
        exclude = ['user']

class EnvThreatsForm(ModelForm):
    class Meta:
        model = EnvThreats
        exclude = ['user']

class TrainersForm(ModelForm):
    class Meta:
        model = AspImpact
        exclude = ['user']

