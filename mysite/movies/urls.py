from django.urls import path

from . import views

app_name='movies'
urlpatterns = [
    path('', views.home, name='home'),
    path('movies/', views.list_movies, name='movies-list'),
    path('theaters/', views.list_theaters, name='theaters-list'),
    path('movies/<int:movie_id>/', views.movie_detail, name="movie-details"),
    path('theaters/<slug:th_id>/', views.theater_detail, name="theater-details"),
    path('movies/<str:movie_genre>/', views.list_movies, name='movies-by-genre'),
    path('movies/<str:movie_genre>/<str:movie_genre1>/', views.list_movies, name='movies-by-complicated-genre'),
    path('api/<slug:slug>/', views.api, name='api'),
]
