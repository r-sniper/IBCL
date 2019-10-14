from django.shortcuts import render

# Create your views here.
from home.models import TShirtSize, Colour, Team, Player


def home(request):
    t_shirt_size = TShirtSize.objects.filter(is_active=True)
    t_shirt_colour = Colour.objects.filter(is_active=True, is_used=False)

    return render(request, 'base.html', {
        'player_size': range(1, 8),
        't_shirt_size': t_shirt_size,
        't_shirt_colour': t_shirt_colour,
    })


def register(request):
    if request.method == "POST":
        team_name = request.POST.get('team_name')
        selected_colour_pk = int(request.POST.get("t_shirt_colour"))
        t_shirt_colour = Colour.objects.get(pk=selected_colour_pk)
        team_obj = Team.objects.create(team_name=team_name, t_shirt_colour=t_shirt_colour)
        t_shirt_colour.is_used = True
        t_shirt_colour.save()
        team_obj.save()
        captain_number = int(request.POST.get("is_captain"))
        for i in range(1, 9):
            print(i)
            player_name = request.POST.get('player_name_' + str(i))
            print_name = request.POST.get('player_print_name_' + str(i))
            t_shirt_number = request.POST.get('player_t_shirt_number_' + str(i))
            t_shirt_size_pk = request.POST.get('player_t_shirt_size_' + str(i))
            t_shirt_obj = TShirtSize.objects.get(pk=t_shirt_size_pk)
            is_captain = False
            if captain_number == i:
                is_captain = True

            print(player_name)
            print(print_name)
            print(t_shirt_number)
            print(t_shirt_size_pk)
            print(t_shirt_obj)
            print(is_captain)
            if player_name != "" and print_name != "" and t_shirt_number != "":
                player_obj = Player.objects.create(player_name=player_name, printing_name=print_name,
                                                   t_shirt_number=t_shirt_number, t_shirt_size=t_shirt_obj,
                                                   is_captain=is_captain, team=team_obj)

                player_obj.save()

        return render(request, 'success.html')
