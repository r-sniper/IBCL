from django.db import models


class Colour(models.Model):
    colour_name = models.CharField(unique=True, max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.colour_name


class TShirtSize(models.Model):
    size = models.CharField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.size


class Player(models.Model):
    player_name = models.CharField(max_length=100)
    printing_name = models.CharField(max_length=100)
    t_shirt_number = models.CharField(max_length=5)
    t_shirt_size = models.ForeignKey(TShirtSize, on_delete=models.CASCADE)

    def __str__(self):
        return self.player_name


class Team(models.Model):
    team_name = models.CharField(max_length=200, unique=True)
    team_captain = models.OneToOneField(Player, on_delete=models.CASCADE,unique=True)
    players = models.ManyToOneRel(Player)

    def __str__(self):
        return self.team_name
