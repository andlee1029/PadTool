# Generated by Django 5.0.6 on 2024-06-05 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaderskill',
            name='lskill_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='monster',
            name='monster_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='skill',
            name='skill_name',
            field=models.CharField(max_length=100),
        ),
    ]
