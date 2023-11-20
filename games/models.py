from django.db import models


class Player(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    rating = models.IntegerField()
    previous_rating = models.IntegerField()


class Game(models.Model):
    player1 = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="games_as_1")
    player2 = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="games_as_2")
    game_type = models.CharField(max_length=100)
    yurishlar = models.IntegerField()
    result_p1 = models.IntegerField()
    result_p2 = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
