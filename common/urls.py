from django.urls import path
from . import views


urlpatterns = [
    path('top-courses', views.TopCoursesView.as_view(), name="top_courses"),
    path('top-books', views.TopBooksView.as_view(), name="top_books"),
    path('last-news', views.LastNewsView.as_view(), name="last_news"),
    path('last-games', views.LastGamesView.as_view(), name="last_games"),
    path('rating', views.RatingPlayersView.as_view(), name="rating_players"),
]
