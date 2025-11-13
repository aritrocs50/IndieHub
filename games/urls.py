from django.urls import path
from .views import GameListCreateView, RatingCreateView

urlpatterns = [
    path('', GameListCreateView.as_view(), name='game-list'),
    path('rate/', RatingCreateView.as_view(), name='rate-game'),
]
