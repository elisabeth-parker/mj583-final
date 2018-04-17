from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/', views.list_movies, name='movies-list'),
    path('theaters/', views.list_theaters, name='theaters-list'),
    path('movies/<int:movie_id>/', views.movie_detail, name="movie-details"),
]
