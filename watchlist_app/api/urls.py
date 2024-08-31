from django.urls import path
from .views import MovieListAV, MovieDetailAV

urlpatterns = [
    
    path('',MovieListAV.as_view(),name='movie-list'),
    path('<int:pk>',MovieDetailAV.as_view(),name='movie-detail'),
]
