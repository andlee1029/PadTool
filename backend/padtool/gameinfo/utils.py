import json
from .models import Monster, Monster_Attribute

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
