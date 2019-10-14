from django.contrib import admin

# Register your models here.
from home.models import TShirtSize, Colour, Team, Player

admin.site.register(TShirtSize)
admin.site.register(Colour)
admin.site.register(Team)
admin.site.register(Player)