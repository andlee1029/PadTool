# Generated by Django 5.0.6 on 2024-06-13 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gameinfo', '0003_rename_skill_activeskill_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='monster_attribute',
            unique_together={('monster_id_monster', 'attribute_number')},
        ),
    ]
