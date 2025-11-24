# movies/views.py
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import Movie, Rating, Review, WatchList, LikeReview
from .serializers import (
    MovieListSerializer, MovieDetailSerializer,
    RatingSerializer, ReviewSerializer, WatchListSerializer, MovieSerializer,UserSerializer,
    UserRegisterSerializer,
)


class MovieListAPIView(generics.ListAPIView):
    queryset = Movie.objects.all().order_by('-id')
    serializer_class = MovieListSerializer


class MovieDetailAPIView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer

    # request 넣어주려고 override
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class RatingCreateUpdateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, movie_pk):
        movie = get_object_or_404(Movie, pk=movie_pk)
        score = request.data.get('score')
        rating, created = Rating.objects.update_or_create(
            user=request.user,
            movie=movie,
            defaults={'score': score},
        )
        serializer = RatingSerializer(rating)
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)


class ReviewListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, movie_pk):
        reviews = Review.objects.filter(movie_id=movie_pk).select_related('user')
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request, movie_pk):
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ReviewDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def put(self, request, review_pk):
        review = get_object_or_404(Review, pk=review_pk, user=request.user)
        serializer = ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, review_pk):
        review = get_object_or_404(Review, pk=review_pk, user=request.user)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewLikeToggleAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, review_pk):
        review = get_object_or_404(Review, pk=review_pk)
        like, created = LikeReview.objects.get_or_create(
            review=review,
            user=request.user,
        )
        if not created:
            # 이미 있으면 토글 off
            like.delete()
            liked = False
        else:
            liked = True
        return Response({'liked': liked, 'like_count': review.likes.count()})


class WatchListToggleAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, movie_pk):
        """
        status를 body로 받고, 없으면 WANT 기본값
        """
        movie = get_object_or_404(Movie, pk=movie_pk)
        status_value = request.data.get('status', 'WANT')

        watch, created = WatchList.objects.update_or_create(
            user=request.user,
            movie=movie,
            defaults={'status': status_value},
        )
        serializer = WatchListSerializer(watch)
        return Response(serializer.data)



class SimilarMovieAPIView(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        movie_id = self.kwargs['movie_id']
        movie = Movie.objects.get(id=movie_id)

        # 간단히: 같은 country 영화 추천 (자기 자신 제외)
        return Movie.objects.filter(country=movie.country).exclude(id=movie.id)

class ReviewListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        movie_id = self.kwargs['movie_id']
        return Review.objects.filter(movie_id=movie_id)

    def perform_create(self, serializer):
        movie_id = self.kwargs['movie_id']
        serializer.save(movie_id=movie_id)
        
class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]


class MeAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
