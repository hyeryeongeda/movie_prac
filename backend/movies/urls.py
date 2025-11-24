# movies/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MovieListAPIView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', views.MovieDetailAPIView.as_view(), name='movie-detail'),
    path('movies/<int:movie_id>/similar/', views.SimilarMovieAPIView.as_view()),
    path('movies/<int:movie_id>/reviews/', views.ReviewListCreateAPIView.as_view()),

    path('movies/<int:movie_pk>/rating/', views.RatingCreateUpdateAPIView.as_view(), name='movie-rating'),
    path('movies/<int:movie_pk>/reviews/', views.ReviewListCreateAPIView.as_view(), name='movie-review-list'),
    path('reviews/<int:review_pk>/', views.ReviewDetailAPIView.as_view(), name='review-detail'),
    path('reviews/<int:review_pk>/like/', views.ReviewLikeToggleAPIView.as_view(), name='review-like'),

    path('movies/<int:movie_pk>/watchlist/', views.WatchListToggleAPIView.as_view(), name='watchlist-toggle'),
    path('movies/<int:movie_id>/similar/', views.SimilarMovieAPIView.as_view()),

]
