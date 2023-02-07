from django.db import models

class Game(models.Model):
    game_50px = models.ImageField(upload_to='images', null=True)
    game_30px = models.ImageField(upload_to='images', null=True)
    game_15px = models.ImageField(upload_to='images', null=True)
    game_2px = models.ImageField(upload_to='images', null=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
