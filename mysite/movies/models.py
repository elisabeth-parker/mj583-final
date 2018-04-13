from django.db import models

class Theater(models.Model):
    address = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 20)



class Movie(models.Model):
    title = models.CharField(max_length = 100)
    movie_id = models.IntegerField()
    runtime = models.IntegerField()
    releaseDate = models.DateField()
    RATINGS = (
        ('G', 'G: General Audiences'),
        ('PG', 'PG: Parental Guidance Suggested'),
        ('PG-13', 'PG-13: Parents Strongly Cautioned'),
        ('R', 'R: Restricted'),
        ('NC-17', 'NC-17: Adults Only'),
    )
    poster = models.CharField(max_length = 200)
    GENRES = (
        ('Comedy', 'Comedy'),
        ('Suspense', 'Suspense/Thriller'),
        ('Drama', 'Drama'),
        ('Action', 'Action/Adventure'),
        ('Sci-Fi', 'Sci-Fi/Fantasy'),
        ('Animated', 'Animated'),
        ('Romance', 'Romance'),
        ('Horror', 'Horror'),
        ('Family', 'Family'),
    )

class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    time = models.DateField()
    tickets = models.CharField(max_length = 250)





# Create your models here.
