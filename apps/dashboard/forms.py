from django import forms
from models import Patient
from django.forms import widgets
from datetime import datetime, date
from django.db import models
from django.forms import ModelForm

# class PatientForm(forms.Form):
#     first_name = forms.CharField(max_length=60)
#     last_name = forms.CharField(max_length=60)
#     age = forms.IntegerField()
#     location = forms.CharField(max_length=30)
#     condition = forms.CharField(widget=forms.TextInput, max_length=150)
#     medication = forms.CharField(max_length=30)
#     initial_visit = forms.DateField(label="Initial Visit Date")
#
#     def save(self, commit=True):
#         patient = super(PatientForm, self).save(commit=False)
#
#         if commit:
#             patient.save()
#             return patient

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'age', 'location', 'condition', 'medication', 'initial_visit', 'followup_appt', 'reminder_freq')
