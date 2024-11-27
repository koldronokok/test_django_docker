from django.urls import path
from . import views

urlpatterns = [
    path('patients/', views.patients_list, name='patients_list'),
    path('doctors/', views.doctors_list, name='doctors_list'),
    path('hospitalizations/', views.hospitalizations_list, name='hospitalizations_list'),
]
