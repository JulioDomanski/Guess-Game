from django.contrib import admin
from .models import Game

# Register your models here.
class ListandoGame(admin.ModelAdmin):
    list_display = ('id', 'game_50px', 'game_30px', 'game_15px', 'game_2px', 'name')


admin.site.register(Game, ListandoGame)