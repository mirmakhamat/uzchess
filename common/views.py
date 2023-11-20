from rest_framework import generics
from courses.models import Course
from courses.serializers import CourseListSerializer
from library.models import Book
from library.serializers import BookListSerializer
from news.models import News
from news.serializers import NewsListSerializer
from games.models import Game, Player
from games.serializers import GameSerializer, PlayerSerializer


class TopCoursesView(generics.ListAPIView):
    queryset = Course.objects.all().order_by('-rating')[:5]
    serializer_class = CourseListSerializer


class TopBooksView(generics.ListAPIView):
    queryset = Book.objects.all().order_by('-rating')[:5]
    serializer_class = BookListSerializer


class LastNewsView(generics.ListAPIView):
    queryset = News.objects.all().order_by('-created_at')[:4]
    serializer_class = NewsListSerializer

class LastGamesView(generics.ListAPIView):
    queryset = Game.objects.all().order_by('-created_at')[:5]
    serializer_class = GameSerializer


class RatingPlayersView(generics.ListAPIView):
    queryset = Player.objects.all().order_by('-rating')[:5]
    serializer_class = PlayerSerializer
