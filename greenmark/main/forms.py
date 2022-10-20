from dataclasses import field
from pyexpat import model
from django.forms import ModelForm

from .models import *

class AgreementDocForm(ModelForm):
    class Meta:
        model = AgreementDoc
        fields = '__all__'

class BussInfoForm(ModelForm):
    class Meta:
        model = BussInfo
        fields = '__all__'

class KeyDecisionMakerForm(ModelForm):
    class Meta:
        model = KeyDecisionMaker
        fields = '__all__'

class EnvironManagerForm(ModelForm):
     class Meta:
        model = EnvironManager
        fields = '__all__'

class OtherResponsiblePersonForm(ModelForm):
    class Meta:
        model = OtherResponsiblePerson
        fields = '__all__'

class EnvCompObligForm(ModelForm):
    class Meta:
        model = EnvCompOblig
        fields = '__all__'

class EnvCommForm(ModelForm):
    class Meta:
        model = EnvComm
        fields = '__all__'