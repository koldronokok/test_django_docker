from django.db import models

class Movies(models.Model):
    title = models.CharField(max_length=100, verbose_name="Назва фільму")
    genre = models.CharField(max_length=50, verbose_name="Жанр")
    duration = models.PositiveIntegerField(verbose_name="Тривалість (хвилини)")
    rating = models.DecimalField(max_digits=3, decimal_places=2, verbose_name="Рейтинг")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фільм"
        verbose_name_plural = "Фільми"


class Cinemas(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва кінотеатру")
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна квитка")
    seats_count = models.PositiveIntegerField(verbose_name="Кількість місць")
    address = models.CharField(max_length=255, verbose_name="Адреса")
    phone = models.CharField(max_length=20, verbose_name="Телефон")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Кінотеатр"
        verbose_name_plural = "Кінотеатри"


class MovieScreenings(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name="screenings", verbose_name="Фільм")
    cinema = models.ForeignKey(Cinemas, on_delete=models.CASCADE, related_name="screenings", verbose_name="Кінотеатр")
    start_date = models.DateField(verbose_name="Дата початку показу")
    screening_duration = models.PositiveIntegerField(verbose_name="Тривалість показу (дні)")

    def __str__(self):
        return f"{self.movie.title} у {self.cinema.name}"

    class Meta:
        verbose_name = "Показ"
        verbose_name_plural = "Покази"
