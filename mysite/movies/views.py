from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.forms.models import model_to_dict
from . import models


def home(request):
    return render(request, "movies/home.html", {
        'theaters': models.Theater.objects.all(),
        'movies': models.Movie.objects.all()
    })

def list_movies(request):
    objects = models.Movie.objects.all()
    return render(request, "movies/list.html", {
        "list_type": "Movies",
        "objects": objects
    })

def list_theaters(request):
    # filter_by = request.GET.get('filter')
    # filter_val = request.GET.get('val')
    # filter_breadcrumb_name = None
    # filter_breadcrumb_url = None

    objects = models.Theater.objects.all()

    # if filter_by and filter_val:
    #     if filter_by == 'city':
    #         objects = objects.filter(movie__city__iexact=filter_val)
    #         filter_breadcrumb_name = "City"
    #         #filter_breadcrumb_url = reverse("winners:countries-list")
    #     if filter_by == 'movie':
    #         for o in objects:
    #             if o.movie_set
    #         objects = objects.filter(movie__genre__iexact=filter_val)
    #         filter_breadcrumb_name = "Genres"
            #filter_breadcrumb_url = reverse("winners:categories-list")

    return render(request, "movies/list.html", {
        "list_type": "Theaters",
        "objects": objects,
        # "filter_by": filter_by,
        # "filter_val": filter_val,
        # "filter_breadcrumb_name": filter_breadcrumb_name,
        # "filter_breadcrumb_url": filter_breadcrumb_url,
    })

def movie_detail(request, movie_id):
      movie = get_object_or_404(models.Movie, movie_id=movie_id)
      theater_objects = movie.theaters.all()
      theaters = []
      for t, theater in enumerate(theater_objects):
          theaters.append(theater)

      context = {
        'title' : movie.title,
        'poster' : "https://" + movie.poster,
        'theaters' : theaters,
        'rating' : movie.rating,
        'runtime' : movie.runtime,
      }
      return render(request, "movies/movie_detail.html", context)

def theater_detail(request, th_id):
      theater = get_object_or_404(models.Theater, th_id=th_id)
      movie_objects = theater.movie_set.all()
      # movies = []
      # for m, movie in enumerate(movie_objects):
      #     movies.append(movie)

      context = {
        'name' : theater.name,
        'address' : theater.address,
        'phone' : theater.phone,
        'movies' : movie_objects,
      }
      return render(request, "movies/theater_detail.html", context)

def api(request, slug):

    if slug == 'movies':
        data = models.Movie.objects.values()
        print("type is movies")
    elif slug == 'showtimes':
        data = models.Showtime.objects.values()
        print("type is showtimes")
    else:
        data = models.Theater.objects.values()
        print("type is other, showing theaters")

    f_data = {"Data": [w for w in data]}

    return JsonResponse(f_data)

# Create your views here.
