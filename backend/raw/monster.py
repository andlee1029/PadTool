import os
import json
from typing import Iterator, Any

from utils import MonsterType, MonsterAttribute

FILE_NAME = 'monster_api.json'

class RawMonster():
    """Representation of PAD monster"""

    def __init__(self, data: list[Any]):
        def _get_curve(iter: Iterator[Any]) -> tuple[int, int, float]:
            # Returns curve which is (min, max, scale)
            return (next(dataIter), next(dataIter), next(dataIter))
        
        dataIter = iter(data)
        self.id: int = next(dataIter)
        self.name: str = next(dataIter)
        
        self.attributes: list[MonsterAttribute] = [MonsterAttribute(next(dataIter))]
        nextAtt = next(dataIter)
        if (nextAtt != -1): self.attributes.append(MonsterAttribute(nextAtt))

        self.isUltEvo:bool = bool(next(dataIter)) #True if is ultimate evo

        self.types: list[MonsterType] = [MonsterType(next(dataIter))]
        nextType = next(dataIter)
        if(nextType != -1): self.types.append(MonsterType(nextType))

        self.rarity: int = next(dataIter)
        self.cost: int = next(dataIter)

        # Related to whether monster spawns alone
        # If 5, always spawns alone
        self.unknown1: int = next(dataIter)

        self.maxLevel: int = next(dataIter)
        self.feedExpPerLevel = next(dataIter)/4 #Have not confirmed
        self.released = (next(dataIter) == 100)
        self.sellPrice = (next(dataIter)/10) #Have not confirmed

        self.hp = _get_curve(dataIter)
        self.atk = _get_curve(dataIter)
        self.rcv = _get_curve(dataIter)
        self.exp: tuple[int, int, float] = (0, next(dataIter), next(dataIter))
        self.askill_id: int = next(dataIter)
        self.lskill_id: int = next(dataIter)

        # maybe turn this into shared type as well
        self.enemy_info = {
            'countdown': next(dataIter),
            'hp': _get_curve(dataIter),
            'atk': _get_curve(dataIter),
            'def': _get_curve(dataIter),
            'maxLevel': next(dataIter),
            'coins_per_level': next(dataIter),
            'exp_per_level': next(dataIter)
        }

        self.prev_evo_id: int = next(dataIter)
        self.evo_materials: list[int] = [next(dataIter) for i in range(5)]
        self.devo_materials: list[int] = [next(dataIter) for i in range(5)]

        # When >0, the enemy turn timer for technical dungeons.
        self.enemy_info['turn_timer'] = next(dataIter)

        # Controls whether the monster uses the 'new' AI or the 'old' AI.
        # Monsters using the old  AI only have support up to some limit of ES values.
        # One main difference between is behavior during preempts; old-AI monsters will
        # attack if they cannot execute a preempt, new-AI monsters will skip to the next.
        # (needs verification).
        self.enemy_info['uses_ai'] = bool(next(dataIter))

        # Each monster has an internal counter which starts at raw[53] and is decremented
        # each time a skill activates. If the counter is less than the action cost, it cannot
        # execute.
        #
        # Turn flow follows this order:
        # 1: pick action (possibly checking counter value)
        # 2: increment the counter up, capped at the max value
        # 3: decrement the counter based on the selected action value
        #
        # The starting and maximum value for the enemy skill action counter.
        self.enemy_info['skill_max_counter'] = next(dataIter)

        # The amount to increment the counter each turn.
        #
        # The vast majority of these are 0/1.
        # Deus Ex Machina has 2, Kanna has 7.
        self.enemy_info['skill_counter_incr'] = next(dataIter)

        # Boolean, unlikely to be anything useful, only populated for 495 (1) and 111 (1000).
        self.unknown2 = next(dataIter)

        #unused
        self.unknown3 = next(dataIter)

        self.enemy_info['num_skills'] = next(dataIter)
        
        #prob make shared type for this as well
        # (id, ai, rnd)
        self.enemy_info['skills'] = [(next(dataIter), next(dataIter), next(dataIter)) for i in range(self.enemy_info['num_skills'])]
        num_awakenings: int = next(dataIter)
        self.awakenings: list[int] = [next(dataIter) for i in range(num_awakenings)]
        self.super_awakenings: list[int] = list(map(int, filter(str.strip, next(dataIter).split(','))))
        self.root_id: int = next(dataIter) #fixing needs to be done?
        self.series_id: int = next(dataIter)

        third_type: int = next(dataIter)
        if (third_type != -1): self.types.append(MonsterType(third_type))

        self.mp_sell_price: int = next(dataIter)
        self.latent_awakening_id: int = next(dataIter) #not sure what this is think only for latent tamadras?
        self.collab_id: int = next(dataIter)

        self.flags = next(dataIter) #ignoring what the flags mean for now

        self.alt_names: list[str] = next(dataIter).split('|')
        self.limit_break_multiplier: int = next(dataIter)

        # 1-indexed 
        self.voice_id: int = next(dataIter)
        orb_or_bgm_id: int = next(dataIter)
        self.orb_skin_id = orb_or_bgm_id if orb_or_bgm_id < 10_000 else 0 
        self.bgm_set_id = orb_or_bgm_id if orb_or_bgm_id >= 10_000 else 0 

        # special attribute unused except for old monster transform values
        self.transform_tag: str = next(dataIter)

        # not conformed what this is for
        self.lskil_bitflag: int = next(dataIter) + (next(dataIter) << 32)

        # 0 for all cards excpet NY cards
        self.unknown4 = next(dataIter)

        # 0 for all cards
        self.unknown5 = next(dataIter)

        #might need to do server mismatch here (inserting -1 if len is 76)

        third_attribute = next(dataIter)
        if (third_attribute != -1): self.attributes.append(MonsterAttribute(third_attribute))

        #mroe fields that i left out

    def get_monster_info(self) -> dict[str, Any]:
        # Returns dictionary of monster info needed for fixtures
        return {
            "model" : "gameinfo.Monster",
            "fields" : {
                "monster_id" : self.id,
                "monster_name" : self.name,
                "askill_id_askill" : self.askill_id,
                "lskill_id_lskill" : self.lskill_id,
                "root_monster" : self.root_id
            }
        }
    
    def get_monster_attributes(self, pkey_id) -> list[dict[str, Any]]:
        return ({
            "model" : "gameinfo.Monster_Attribute",
            "fields" : {
                "monster_att_id" : pkey_id,
                "monster_id_monster" : self.id,
                "monster_attribute" : att.name,
                "attribute_number" : ind + 1
            }
        } for ind, att in enumerate(self.attributes))
    
    def get_monster_types(self, pkey_id) -> list[dict[str,Any]]:
        return({
            "model" : "gameinfo.Monster_Type",
            "fields" : {
                "monster_type_id" : pkey_id,
                "monster_id_monster" : self.id,
                "monster_type" : monster_type.name,
                "type_number" : ind + 1
            }
        } for ind, monster_type in enumerate(self.types))

    def __str__(self):
        return '''
            ID: {}\n
            Name: {}\n
            Attributes: [{}]\n
            Types: [{}]\n
            Skill ID: {}\n
            Leader Skill ID: {}\n
            Ancestor ID: {}\n
            Root ID: {}\n
        '''.format(self.id, self.name, " ".join(list(map(str, self.attributes))), " ".join(list(map(str, self.types))), self.askill_id, self.lskill_id, self.prev_evo_id, self.root_id)


    
def load_monster_data(dir: str = 'raw-data/', fileLocation: str = FILE_NAME) -> list[RawMonster]:
    """Loads monsters from raw data file"""

    file_path = os.path.join(dir, fileLocation)
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    monsters = [RawMonster(m) for m in data['card']]
    return monsters