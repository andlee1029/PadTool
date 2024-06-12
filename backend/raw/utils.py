from enum import Enum

class MonsterAttribute(Enum):
    FIRE = 0
    WATER = 1
    WOOD = 2
    LIGHT = 3
    DARK = 4
    EMPTY = 6

class MonsterType(Enum):
    EVO_MATERIAL = 0
    BALANCED = 1
    PHYSICAL = 2
    HEALER = 3
    DRAGON = 4
    GOD = 5
    ATTACKER = 6
    DEVIL = 7
    MACHINE = 8
    AWAKEN_MATERIAL = 12
    ENHANCE_MATERIAL = 14
    REDEEMABLE_MATERIAL = 15
