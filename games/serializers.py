from rest_framework import serializers
from .models import Game, Rating

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['user', 'rating', 'comment', 'created_at']

class GameSerializer(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = ['id', 'title', 'description', 'genre', 'developer', 'file', 'screenshot', 'trailer_url', 'created_at', 'ratings']
