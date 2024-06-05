import json
import os
import sys
sys.path.append(os.getcwd())

from monster import load_monster_data
from skill import load_skill_data

monsters = load_monster_data()
stripped_monsters = []

for mons in monsters:
    stripped_monsters.append({
        "monster_id" : mons.id,
        "monster_name" : mons.name,
        "skill_id_skill" : mons.skill_id,
        "lskill_id_lskill" : mons.lskill_id,
        "root_monster" : mons.root_id
    })

monsters_json = json.dumps(stripped_monsters)

with open('padtool/fixtures/monsters.json', 'w') as f:
    f.write(monsters_json)

active_skills, leader_skills = load_skill_data()
stripped_active_skills = []
stripped_leader_skills = []

for askill in active_skills:
    stripped_active_skills.append({
        "skill_id" : askill.id,
        "skill_name" : askill.name,
        "skill_desc" : askill.text,
        "turns": askill.max_cooldown
    })

for lskill in leader_skills:
    stripped_leader_skills.append({
        "lskill_id" : lskill.id,
        "lskill_name" : lskill.name,
        "lskill_desc" : lskill.text
    })

active_skills_json = json.dumps(stripped_active_skills)
leader_skills_json = json.dumps(stripped_leader_skills)

with open('padtool/fixtures/active_skills.json', 'w') as f:
    f.write(active_skills_json)

with open('padtool/fixtures/leader_skills.json','w') as f:
    f.write(leader_skills_json)