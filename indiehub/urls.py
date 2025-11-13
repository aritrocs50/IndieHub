from django.contrib import admin
from django.urls import path, include
from indiehub.views import home, game_detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('game/<int:pk>/', game_detail, name='game-detail'),
    path('admin/', admin.site.urls),
    path('api/games/', include('games.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)