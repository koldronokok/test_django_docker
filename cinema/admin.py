from django.contrib import admin
from .models import Movies, Cinemas, MovieScreenings

admin.site.register(Movies)
admin.site.register(Cinemas)
admin.site.register(MovieScreenings)
