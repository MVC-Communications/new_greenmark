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
        fields = '__all__'

class AspImpactForm(ModelForm):
    class Meta:
        model = AspImpact
        exclude = ['user']