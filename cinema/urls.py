from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movies_list, name='movies_list'),
    path('cinemas/', views.cinemas_list, name='cinemas_list'),
    path('screenings/', views.screenings_list, name='screenings_list'),
]
