# Generated by Django 5.0.6 on 2024-06-14 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameinfo', '0004_alter_monster_attribute_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster_attribute',
            name='monster_attribute',
            field=models.SmallIntegerField(choices=[(0, 'FIRE'), (1, 'WATER'), (2, 'WOOD'), (3, 'LIGHT'), (4, 'DARK'), (6, 'EMPTY')]),
        ),
        migrations.AlterField(
            model_name='monster_type',
            name='monster_type',
            field=models.SmallIntegerField(choices=[(0, 'EVO_MATERIAL'), (1, 'BALANCED'), (2, 'PHYSICAL'), (3, 'HEALER'), (4, 'DRAGON'), (5, 'GOD'), (6, 'ATTACKER'), (7, 'DEVIL'), (8, 'MACHINE'), (12, 'AWAKEN_MATERIAL'), (14, 'ENHANCE_MATERIAL'), (15, 'REDEEMABLE_MATERIAL')]),
        ),
    ]