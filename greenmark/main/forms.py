from dataclasses import field
from pyexpat import model
from django.forms import ModelForm
from django import forms

from .models import *

class BussInfoForm(ModelForm):
    class Meta:
        model = BussInfo
        exclude = ['user']
class EnvCompObligForm(ModelForm):
    # person_rep = forms.ChoiceField(widget=forms.RadioSelect(choices=PERSON_RESP_FOR_ENV_COMP))
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

class ObjectivesForm(ModelForm):
    class Meta:
        model = Objectives
        exclude = ['user']

class CompanyPolicyForm(ModelForm):
    class Meta:
        model = CompanyPolicy
        exclude = ['user']

class EmergencyResponseForm(ModelForm):
    class Meta:
        model = EmergencyResponse
        exclude = ['user']

class CommunicationsForm(ModelForm):
    class Meta:
        model = Communications
        exclude = ['user']

class DocumentationForm(ModelForm):
    class Meta:
        model = Documentation
        exclude = ['user']

class AuditReviewForm(ModelForm):
    class Meta:
        model = AuditReview
        exclude = ['user']

class LocationForm(ModelForm):
    class Meta:
        model = Location
        exclude = ['user']