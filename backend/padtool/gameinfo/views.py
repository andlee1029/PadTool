import sys
from django.http import HttpResponse
from django.shortcuts import render
from .models import Monster, Monster_Attribute, Monster_Type
from .utils import print_monster
from .forms import MonsterSearchForm

sys.path.append("..")
from images.image_util import get_image


def index_2(request):
    context = {
        "monsters" : [],
        "attributes" : Monster_Attribute.Attribute.choices,
        "types" : Monster_Type.Type.choices,
    }

    if request.method == "POST":
        print("received post reqest with request")
        print(request.POST)
        form = MonsterSearchForm()
    else:
        form = MonsterSearchForm()


    context["form"] = form
    return render(request, "gameinfo/request.html", context)

def index(request):
    monsters = Monster.objects.all()
    attributes = []
    for monster in monsters:
        monster_attribute_objects = Monster_Attribute.objects.filter(monster_id_monster = monster.monster_id)
        monster_attributes = [0] * len(monster_attribute_objects)
        for mon_att_obj in monster_attribute_objects:
            monster_attributes[mon_att_obj.attribute_number - 1] = mon_att_obj.monster_attribute
        attributes.append(monster_attributes)
    monster_images = []
    for ind, monster in enumerate(monsters):
        monster_id = monster.monster_id
        new_image_path = 'gameinfo/static/gameinfo/monster_pic'+ str(monster_id) + '.PNG'
        get_image(monster_id, attributes[ind], new_image_path)
        monster_images.append('gameinfo/monster_pic' + str(monster_id) + '.PNG')
    # monsters = ["hello"] * len(monster_images)
    monster_image_pairs = [(monster, monster_images[ind]) for ind, monster in enumerate(monsters)]
    context = {
        "monsters" : monster_image_pairs,
        "attributes" : Monster_Attribute.Attribute.choices,
        "types" : Monster_Type.Type.choices,
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



