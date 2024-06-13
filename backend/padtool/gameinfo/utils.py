import json

from .models import Monster, ActiveSkill, LeaderSkill, Monster_Attribute

def print_monster(monster: Monster) -> str:
    askill = monster.askill_id_askill
    lskill = monster.lskill_id_lskill

    return json.dumps({
        "monster_id" : monster.monster_id,
        "monster_name" : monster.monster_name,
        "active_skill_name" : askill.askill_name,
        "active_skill_desc" : askill.askill_desc,
        "leader_skill_name" : lskill.lskill_name,
        "leader_skill_desc" : lskill.lskill_desc,
    })

def attribute_to_num(att: Monster_Attribute) -> int:
    if att == "FIRE": return 0
    if att == "WATER": return 1
    if att == "WOOD": return 2
    if att == "LIGHT": return 3
    if att == "DARK": return 4
    if att == "EMPTY": return 6
    return -1
