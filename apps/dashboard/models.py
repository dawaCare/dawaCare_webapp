# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    age = models.PositiveSmallIntegerField()
    location = models.CharField(max_length=30)
    condition = models.CharField(max_length=150)
    medication = models.CharField(max_length=30)
    initial_visit = models.DateField()
    followup_appt = models.DateField()
    reminder_freq = models.PositiveIntegerField()
