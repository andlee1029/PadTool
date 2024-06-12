from django.contrib import admin
from .models import Monster, ActiveSkill, LeaderSkill, Monster_Attribute, Monster_Type
# Register your models here.
admin.site.register([Monster, ActiveSkill, LeaderSkill, Monster_Type, Monster_Attribute])