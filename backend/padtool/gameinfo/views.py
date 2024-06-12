from django.http import HttpResponse
from django.shortcuts import render
from .models import Monster
from .utils import print_monster

def index(request):
    context = {
        "monsters" : Monster.objects.all()
    }
    return render(request, "gameinfo/request.html", context)

def monster(request, monster_id):
    try:
        monster = Monster.objects.get(monster_id=monster_id)
        response = "Returning monster of id {}\n".format(monster_id)
        response += print_monster(monster)
    except Monster.DoesNotExist as err:
        response = str(err) + ('\n for id {}'.format(monster_id))
    return HttpResponse(response)