from django.db import models


class Patients(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    birth_year = models.IntegerField()
    category = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    pass

class Doctor(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=50)
    experience = models.IntegerField()

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.specialization})"

class Hospitalization(models.Model):
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    admission_date = models.DateField()
    days_in_hospital = models.IntegerField()
    treatment_cost = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f"Госпіталізація пацієнта {self.patient} з {self.admission_date}"
