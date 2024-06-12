import json
import os
import sys
sys.path.append(os.getcwd())

from monster import load_monster_data, RawMonster
from skill import load_skill_data
from player_data import load_player_data


# write fixtures for owned monsters
owned_ids: set[int] = set(load_player_data('raw/raw-data/'))
root_ids: set[int] = set()
askill_ids: set[int] = set()
lskill_ids: set[int] = set()
owned_monsters: list[RawMonster] = []

monsters: list[RawMonster] = load_monster_data('raw/raw-data/')
for mon in monsters:
    if (mon.id in owned_ids) or (mon.root_id in root_ids):
        if (mon.id in owned_ids): root_ids.add(mon.root_id)
        owned_monsters.append(mon)
        askill_ids.add(mon.askill_id)
        lskill_ids.add(mon.lskill_id)

monster_dicts = [m.get_monster_info() for m in owned_monsters]
monsters_json = json.dumps(monster_dicts)
with open('padtool/gameinfo/fixtures/monsters.json', 'w') as f:
    f.write(monsters_json)

# write fixtures for leader skills and active skills
active_skills, leader_skills = load_skill_data('raw/raw-data/')
active_skills_dicts = [askill.get_active_skill_info() for askill in active_skills if askill.id in askill_ids]
leader_skills_dicts = [lskill.get_leader_skill_info() for lskill in leader_skills if lskill.id in lskill_ids]
active_skills_json = json.dumps(active_skills_dicts)
leader_skills_json = json.dumps(leader_skills_dicts)
with open('padtool/gameinfo/fixtures/active_skills.json', 'w') as f:
    f.write(active_skills_json)

with open('padtool/gameinfo/fixtures/leader_skills.json','w') as f:
    f.write(leader_skills_json)

# write fixtures for monster to attribute relationship
att_pkey = 1
monster_attribute_dicts = []
for mon in owned_monsters:
    monster_attribute_dicts.extend(mon.get_monster_attributes(att_pkey))
    att_pkey += 1
monster_attribute_json = json.dumps(monster_attribute_dicts)
with open('padtool/gameinfo/fixtures/monster_attribute.json', 'w') as f:
    f.write(monster_attribute_json)

# write fixtures for monster to type relationship
monster_type_dicts = []
type_pkey = 1
for mon in owned_monsters:
    monster_type_dicts.extend(mon.get_monster_types(type_pkey))
    type_pkey += 1
monster_type_json = json.dumps(monster_type_dicts)
with open('padtool/gameinfo/fixtures/monster_type.json', 'w') as f:
    f.write(monster_type_json)
