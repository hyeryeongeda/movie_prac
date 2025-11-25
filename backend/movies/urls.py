from django.urls import path
from .views import (
    MovieListAPIView, MovieDetailAPIView,
    RatingCreateUpdateAPIView,
    ReviewListCreateAPIView, ReviewLikeToggleAPIView,
    WatchListToggleAPIView, SimilarMovieAPIView, MyWatchListAPIView,
)

urlpatterns = [
    path('movies/', MovieListAPIView.as_view()),
    path('movies/<int:pk>/', MovieDetailAPIView.as_view()),
    path('movies/<int:movie_pk>/rating/', RatingCreateUpdateAPIView.as_view()),
    path('movies/<int:movie_id>/reviews/', ReviewListCreateAPIView.as_view()),
    path('reviews/<int:review_pk>/like/', ReviewLikeToggleAPIView.as_view()),
    path('movies/<int:movie_pk>/watchlist-toggle/', WatchListToggleAPIView.as_view()),
    path('movies/<int:movie_id>/similar/', SimilarMovieAPIView.as_view()),
    path('watchlist/me/', MyWatchListAPIView.as_view()),
]
