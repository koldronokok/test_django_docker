from django.shortcuts import render

from .models import Patients, Doctor, Hospitalization


def patients_list(request):
    patients = Patients.objects.all()
    return render(request, "patients_list.html", {"patients": patients})

def doctors_list(request):
    doctors = Doctor.objects.all()
    return render(request, "doctors_list.html", {"doctors": doctors})

def hospitalizations_list(request):
    hospitalizations = Hospitalization.objects.all()
    return render(request, "hospitalizations_list.html", {"hospitalizations": hospitalizations})
