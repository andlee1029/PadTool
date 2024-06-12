from raw import monster
from raw import skill
from raw import player_data
import os

def test_monster(mon):
    for ind, m in enumerate(mon):
        print(ind, " ", m)

def is_new(mon):
    for t in mon.types:
        if t not in set([0,1,2,3,4,5,6,7,8,12,14,]): return True
    return False

# print("hellow")
monsters = monster.load_monster_data('raw/raw-data/')
for mon in monsters:
    if is_new(mon): print(mon)
# for mon in monsters:
#     # if mon.id == 7173:
#     print(mon)
# monster = [7173,"Drillspear Jade Conqueror, Nautilus",2,1,0,8,2,9,53,5,99,9300,100,9600,2450,11541,1,488,12745,1,11,170,1,5000000,2.5,21767,21770,2,6060,181800,1,273,8190,1,124,1240,1,10,15264,4300,0,0,0,0,0,0,155,156,157,158,159,0,0,0,0,0,0,0,8,28,53,118,118,107,107,109,109,"",7173,100,6,75000,0,0,2,"Fest Exclusive|Transforming Robots",0,0,0,"",39846402,0,0,0,2,0]
# monster1 = [11054,"Mixologist, Baddie",4,0,0,7,1,7,40,5,99,7050,100,7350,1128,6067,1,571,3216,1,86,634,1,5000000,2.5,42282,42288,2,5985,179550,1,251,7530,1,94,940,1,10,8960,1967,0,0,0,0,0,0,155,156,157,158,159,0,0,0,0,0,0,0,9,52,56,56,106,114,114,44,129,63,"56,59,68,130",11054,45,-1,50000,0,0,99,"The Chalice of Ages and the Divine Droplets",30,2049,0,"",35652609,0,8192,0,2,0]
# monster2 = [5849,"Great Witch of Fresh Snow, Reeche",3,1,0,7,1,9,35,5,99,6600,100,6900,916,5595,1,398,2800,1,128,690,1,20000000,2.5,15619,15622,2,5970,179100,1,246,7380,1,88,880,1,10,10080,2842,0,0,0,0,0,0,155,156,157,158,159,0,0,0,0,0,0,0,9,52,56,28,107,107,113,113,97,51,"53,108,55,33,34,80",5849,61,-1,75000,0,0,3,"New Year|Holiday",30,0,0,"",17826821,0,1,0,-1,0],[5850,"Auspicious Magical Hat, Frow",3,-1,0,7,-1,10,100,5,99,16500,100,16800,916,5595,1,398,2800,1,128,690,1,20000000,2.5,15619,0,2,6300,189000,1,345,10350,1,220,2200,1,10,32000,10007,5849,3911,3971,1328,1328,1328,155,156,157,158,159,0,0,0,0,0,0,0,8,49,52,28,54,53,46,46,1,"",5849,61,-1,75000,0,0,3,"New Year|Holiday|Great Witch of Fresh Snow, Reeche",0,0,0,"",0,0,1,0,-1,0]
# # test_monster(monster2)
# # test_monster(monster1)
# test_monster(monster)



# cards = player_data.load_player_data()
# print(cards)












'''
NExt steps
decide what query iw ant to be able to run
populate other tables with general info
populate my omnster box


want to be able to run a = select monster id where att = green
b = select monster id where awakenings = a1 and a2 
intersect a and b
and display



fixtures to build out
MonsterType
monster_attribute
awakening
monsterawakeining


'''