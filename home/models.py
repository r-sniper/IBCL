from django.db import models


class Colour(models.Model):
    colour_name = models.CharField(unique=True, max_length=100)
    is_active = models.BooleanField(default=True)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return self.colour_name


class TShirtSize(models.Model):
    size = models.CharField(unique=True, max_length=4)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.size


class Team(models.Model):
    team_name = models.CharField(max_length=200, unique=True)
    t_shirt_colour = models.OneToOneField(Colour, on_delete=models.CASCADE)
    slogan_submitted = models.BooleanField(default=False)
    slogan = models.CharField(max_length=500)
    def __str__(self):
        return self.team_name


class Player(models.Model):
    player_name = models.CharField(max_length=100)
    printing_name = models.CharField(max_length=100)
    t_shirt_number = models.CharField(max_length=5)
    t_shirt_size = models.ForeignKey(TShirtSize, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    is_captain = models.BooleanField(default=False)

    def __str__(self):
        return self.player_name

class Instruction(models.Model):
    instructions  = models.TextField(max_length=1000)
