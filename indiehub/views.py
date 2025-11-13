from django.shortcuts import render
from games.models import Game

def home(request):
    games = Game.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'games': games})

def game_detail(request, pk):
    game = Game.objects.get(pk=pk)
    return render(request, 'game_detail.html', {'game': game})
