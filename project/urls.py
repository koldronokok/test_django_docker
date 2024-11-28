from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Шлях до адміністративної панелі Django
    path('', include('cinema.urls')),  # Підключення маршрутизації для додатку cinema
]
