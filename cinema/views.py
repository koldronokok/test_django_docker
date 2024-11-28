from django.shortcuts import render
from .models import Movies, Cinemas, MovieScreenings

def movies_list(request):
    movies = Movies.objects.all()
    return render(request, "movies_list.html", {"movies": movies})

def cinemas_list(request):
    cinemas = Cinemas.objects.all()
    return render(request, "cinemas_list.html", {"cinemas": cinemas})

def screenings_list(request):
    screenings = MovieScreenings.objects.select_related("movie", "cinema")
    return render(request, "screenings_list.html", {"screenings": screenings})
