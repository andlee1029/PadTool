import os
import json


FILE_NAME = 'skill_api.json'

class Active_Skill():
    def __init__(self, id, data):
        self.id: int = id
        self.name: str = data[0]
        self.text: str = data[1]

        # type may mean need to parse other fields
        self.skill_type: int = data[2]

        self.max_level: int = data[3] if data[3] != 0 else -1
        self.max_cooldown: int = data[4] if self.max_level != -1 else -1
        self.unknown1: str = data[5]
        self.remaining_data: list[str | int] = data[6:] 

    def get_active_skill_info(self):
        return {
            "model" : "gameinfo.ActiveSkill",
            "fields" : {
                "askill_id" : self.id,
                "askill_name" : self.name,
                "askill_desc" : self.text,
                "turns" : self.max_cooldown - self.max_level + 1
            }
        }

    def __str__(self):
        return '''
            ID: {}\n
            Name: {}\n
            Description: {}\n
        '''.format(self.id, self.name, self.text)


class Leader_Skill():
    def __init__(self, id, data):
        self.id: int = id
        self.name: str = data[0]
        self.text: str = data[1]

        # type may mean need to parse other fields
        self.skill_type: int = data[2]

        self.max_level: int = data[3] if data[3] != 0 else -1
        self.max_cooldown: int = data[4] if self.max_level != -1 else -1
        self.unknown1: str = data[5]
        self.remaining_data: list[str | int] = data[6:]  

    def get_leader_skill_info(self):
        return {
            "model" : "gameinfo.LeaderSkill",
            "fields" : {
                "lskill_id" : self.id,
                "lskill_name" : self.name,
                "lskill_desc" : self.text
            }
        }   
    
    def __str__(self):
        return '''
            ID: {}\n
            Name: {}\n
            Description: {}\n
        '''.format(self.id, self.name, self.text)


def load_skill_data(directory = 'raw-data/', file_name = FILE_NAME) -> tuple[list[Active_Skill], list[Leader_Skill]]:
    file_path = os.path.join(directory, file_name)
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    skill_data = data['skill']
    active_skills = []
    leader_skills = []
    for ind, skill in enumerate(skill_data):
        # for now will just create a leader skill and active skill of that type but will later need to parse the skill type to determine
        active_skills.append(Active_Skill(ind, skill))
        leader_skills.append(Leader_Skill(ind, skill))

    return active_skills, leader_skills