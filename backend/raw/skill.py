import os
import json

from common.pad_types import Active_Skill, Leader_Skill

FILE_NAME = 'skill_api.json'


def load_skill_data(directory = 'raw-data/', file_name = FILE_NAME):
    print("xd1")
    file_path = os.path.join(directory, file_name)
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    print("xd2")
    skill_data = data['skill']
    active_skills = []
    leader_skills = []
    for ind, skill in enumerate(skill_data):
        # for now will just create a leader skill and active skill of that type but will later need to parse the skill type to determine
        active_skills.append(Active_Skill(ind, skill))
        leader_skills.append(Leader_Skill(ind, skill))

    return active_skills, leader_skills