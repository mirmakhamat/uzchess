from rest_framework import generics
from courses.models import Course
from courses.serializers import CourseListSerializer
from library.models import Book
from library.serializers import BookListSerializer
from news.models import News
from news.serializers import NewsListSerializer
from games.models import Game, Player
from games.serializers import GameSerializer, PlayerSerializer

from rest_framework.response import Response


class MainView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        course = Course.objects.all().order_by('-rating')[:5]
        course_data = CourseListSerializer(course, many=True).data
        book = Book.objects.all().order_by('-rating')[:5]
        book_data = BookListSerializer(book, many=True).data
        news = News.objects.all().order_by('-created_at')[:4]
        news_data = NewsListSerializer(news, many=True).data
        game = Game.objects.all().order_by('-created_at')[:5]
        game_data = GameSerializer(game, many=True).data
        player = Player.objects.all().order_by('-rating')[:5]
        player_data = PlayerSerializer(player, many=True).data
        data = {
            'course': course_data,
            'book': book_data,
            'news': news_data,
            'game': game_data,
            'player': player_data
        }
        return Response(data)
