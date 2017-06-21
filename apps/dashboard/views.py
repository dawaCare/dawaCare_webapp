# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import PatientForm
from apps.dashboard.models import Patient
# from apps.walls.models import Patient

# Create your views here.

class IndexView(View):
    def get(self, request):
        patients = Patient.objects.all()
        print (patients)
        context = {
            'patients': patients,
        }
        return render(request, "dashboard/index.html", context)

class PatientView(View):
    form = PatientForm
    def get(self, request):
        context = { "patientForm": self.form()}
        return render(request, "dashboard/new.html", context)
    def post(self, request):
        form = self.form(request.POST)

        print form
        # print request.POST
        print form.is_valid()
        print form.errors

        if form.is_valid():
            form.save()
            return redirect('/patients')
        else:
            context = {'patientForm': form}
            return render(request, 'dashboard/new.html', context)
