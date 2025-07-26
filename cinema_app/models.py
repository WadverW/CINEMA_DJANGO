from django.db import models
from django.utils.text import slugify

class Cinema(models.Model):
    theatre_name = models.CharField(max_length=100)
    slug = models.SlugField()
    address = models.TextField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=100)
    map_coordinates = models.CharField( max_length=50, blank=True, help_text="Координаты для карты")

    def __str__(self):
        return self.theatre_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.theatre_name)
        super().save(*args, **kwargs)


class Hall(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    hall_number = models.PositiveSmallIntegerField("hall number")
    seat_qty = models.PositiveIntegerField("seat quantity")

    def __str__(self):
        return f"{self.hall_number} ({self.cinema.theatre_name})"


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release = models.DateField()
    is_3d = models.BooleanField(default=False)
    is_imax = models.BooleanField(default=False)
    poster = models.ImageField(upload_to='posters/')

    def __str__(self):
        return self.title


class Screening(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    showtime = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.movie.title} - {self.showtime}"


class Seat(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    row = models.CharField(max_length=5)
    number = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.row}{self.number} ({self.hall.hall_number})"