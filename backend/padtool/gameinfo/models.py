from django.db import models
# TODO GO THROUGH AND FIX MANY TO MANY AND ONE TO ONE RELATIONSHIPS


class Skill(models.Model):
    # TODO: ADD FUNCITONALITY OF MONSTER CHANGING AND SKILLE VOLVES
    skill_id = models.BigIntegerField(primary_key=True)
    skill_name = models.CharField(max_length=60)
    skill_desc = models.TextField(blank=True)
    turns = models.IntegerField()

class LeaderSkill(models.Model):
    # TODO: ADD FUNCTIONALITY OF BEING ABLE TO TELL IF 7X6
    lskill_id = models.BigIntegerField(primary_key=True)
    lskill_name = models.CharField(max_length=60)
    lskill_desc = models.TextField(blank=True)

class Monster(models.Model):
    monster_id = models.BigIntegerField(primary_key=True)
    monster_name = models.CharField(max_length=60)
    skill_id_skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    lskill_id_lskill = models.ForeignKey(LeaderSkill, on_delete=models.CASCADE)
    root_monster = models.ForeignKey("Monster", on_delete=models.CASCADE)

class Monster_Type(models.Model):
    MonsterType = models.TextChoices("MonsterType",
        "God Dragon Devil Machine Balanced Attacker Physical Evo-Material Awaken-Material Redeemable-Material Enhance-Material",
    ) 
    monster_type_id = models.BigAutoField(primary_key=True)
    monster_id_monster = models.ForeignKey(Monster, on_delete=models.CASCADE)
    monster_type = models.CharField(blank=False, choices=MonsterType, max_length=20)
    
    class Meta:
        managed = True
        unique_together = (('monster_id_monster','monster_type'),)

class Monster_Attribute(models.Model):
    AttributeType = models.TextChoices("AttributeType",
        "Fire Water Wood Light Dark None",
    )
    monster_att_id = models.BigAutoField(primary_key=True)
    monster_id_monster = models.ForeignKey(Monster, on_delete=models.CASCADE)
    monster_attribute = models.CharField(blank=False, choices=AttributeType, max_length=10)
    attribute_number = models.IntegerField()

    class Meta:
        managed = True
        unique_together = (('monster_id_monster', 'monster_attribute', 'attribute_number'),)

class Awakening(models.Model):
    awakening_id = models.AutoField(primary_key=True)
    awakening_name = models.CharField(max_length=15)
    awakening_desc = models.TextField(blank=True)

class MonsterAwakening(models.Model):
    monster_awakening_id = models.BigAutoField(primary_key=True)
    monster_id_monster = models.ForeignKey(Monster, on_delete=models.CASCADE)
    awakening_id_awakening = models.ForeignKey(Awakening, on_delete=models.CASCADE)
    count = models.IntegerField()

    class Meta:
        managed = True
        unique_together = (('monster_id_monster', 'awakening_id_awakening'),)


