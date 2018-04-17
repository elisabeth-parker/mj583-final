from django.db import models

class Theater(models.Model):
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    name = models.CharField(max_length=100, default = "A Theater!")
    th_id = models.CharField(max_length=10, unique=True)
    lat = models.DecimalField(max_digits=10,decimal_places=4, null=True)
    long = models.DecimalField(max_digits=10,decimal_places=4, null=True)
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.name + ' (' + self.th_id + ')'

class Movie(models.Model):
    title = models.CharField(max_length=100)
    theaters = models.ManyToManyField(Theater)
    movie_id = models.IntegerField(unique=True)
    runtime = models.IntegerField()
    releaseDate = models.DateField()
    poster = models.URLField()
    rating = models.CharField(max_length=10, null=True)
    movie_genre = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title + ' (' + str(self.movie_id) + ')'
    # RATINGS = (
    #     ('G', 'G: General Audiences'),
    #     ('PG', 'PG: Parental Guidance Suggested'),
    #     ('PG-13', 'PG-13: Parents Strongly Cautioned'),
    #     ('R', 'R: Restricted'),
    #     ('NC-17', 'NC-17: Adults Only'),
    # )
    # GENRES = (
    #     ('Comedy', 'Comedy'),
    #     ('Suspense', 'Suspense/Thriller'),
    #     ('Drama', 'Drama'),
    #     ('Action', 'Action/Adventure'),
    #     ('Sci-Fi', 'Sci-Fi/Fantasy'),
    #     ('Animated', 'Animated'),
    #     ('Romance', 'Romance'),
    #     ('Horror', 'Horror'),
    #     ('Family', 'Family'),
    # )

class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE, default="")
    time = models.CharField(max_length = 8)
    tickets = models.CharField(max_length = 250)

    def __str__(self):
        return self.movie.title + ' / ' + self.theater.name + ' / ' + self.time
