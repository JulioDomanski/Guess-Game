from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound
from .models import Game
import random
from django.http import JsonResponse
  

def index(request):
    all_games = list(Game.objects.all())
    games_list = Game.objects.all()
    chosen_game = random.sample(all_games, 1)[0]
    random_game_id = chosen_game.id
    selected_game = get_object_or_404(Game, id=random_game_id)
    response = render(request, 'index.html', {'game': selected_game, 'games_list': games_list })
    response.set_cookie('attempts', 1)
    return response


def check(request, id):
    game = get_object_or_404(Game, id=id)
    attempts = int(request.COOKIES.get('attempts', 1))
    if request.method == 'POST':
        guess = request.POST.get('guess', '')
        if guess.lower() != game.name.lower():
            if attempts == 1:
                image_url = game.game_30px.url
                message = 'Wrong guess!!!'
            elif attempts == 2:
                image_url = game.game_15px.url
                message = 'Wrong guess!!!'
            elif attempts == 3:
                image_url = game.game_2px.url
                message = 'Wrong guess!!!'
            elif attempts == 4:
                image_url = game.game_2px.url
                message = 'Game Over!!!'
            else:
                response = redirect('index')
                response.delete_cookie('attempts')
                return response
            
            data = {
                'result': 'incorrect',
                'message': message,
                'image_url': image_url,
                'attempts': attempts
                }
            attempts += 1
        else:
            image_url = game.game_2px.url
            data = {
                'result': 'correct',
                'image_url': image_url
            }
            attempts = 1
        response = JsonResponse(data)
        response.set_cookie('attempts', attempts)
        return response
    else:
        return HttpResponseNotFound("Not Found")

