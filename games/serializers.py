from rest_framework import serializers
from .models import Game, Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
    player1 = PlayerSerializer()
    player2 = PlayerSerializer()

    class Meta:
        model = Game
        fields = '__all__'
